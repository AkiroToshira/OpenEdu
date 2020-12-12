from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Articles(models.Model):
    articles_data = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=200)
    img = models.ImageField(upload_to='article', blank=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=30, blank=True)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=30, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    document = models.FileField(upload_to='document/', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'lessont/lesson/{self.lesson}'


class Document(models.Model):
    description = models.CharField(max_length=20, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class StudentsGroup(models.Model):
    name = models.CharField(max_length=10)
    lessons = models.ManyToManyField(Lesson, blank=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=10)
    curator = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)


class StudentGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def students_by_group(cls, group):
        students = cls.objects.all().filter(group=group)
        users = User.objects.all().filter(id__in=students)
        return users

    def get_grades(self):
        get_grade = Grade.objects.all().filter(user=self)
        return get_grade


class GradeBook(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def add_new_column(self, date):
        new_column = BookColumn(gradebook=self, date=date)
        new_column.save()

    def get_grades(self):
        get_students = StudentGroup.students_by_group(self.group)
        get_colums = BookColumn.objects.all().filter(gradebook=self)
        grades = []
        for student in get_students:
            grades.append(Grade.objects.all().filter(user=student, date__in=get_colums))
        return grades


class StudentGroupLesson(models.Model):
    lesson = models.ForeignKey(Lesson, blank=False, on_delete=models.CASCADE)
    student_group = models.ForeignKey(Group, blank=False, on_delete=models.CASCADE)
    gradebook = models.ForeignKey(GradeBook, blank=True, null=True, on_delete=models.CASCADE)


@receiver(pre_save, sender=StudentGroupLesson)
def create_gradebook(sender, instance, **kwargs):
    new_gradebook = GradeBook(group=instance.student_group)
    new_gradebook.save()
    instance.gradebook = new_gradebook


class BookColumn(models.Model):
    date = models.DateField(blank=False)
    gradebook = models.ForeignKey(GradeBook, blank=True, on_delete=models.CASCADE)

    @classmethod
    def get_column_grade(cls, column_id):
        get_column = Grade.objects.all().filter(date=column_id)
        return get_column

    def get_grade(self):
        get_grade = Grade.objects.all().filter(date=self.id)
        return get_grade


class Grade(models.Model):
    date = models.ForeignKey(BookColumn, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=3, default='')


@receiver(post_save, sender=BookColumn)
def create_grade(sender, instance, created, **kwargs):
    if created:
        gradebook = instance.gradebook
        students = StudentGroup.students_by_group(group=gradebook.group)
        for student in students:
            new_grade = Grade(date=instance, user=User.objects.get(id=student.id))
            new_grade.save()


class Deadlines(models.Model):
    name = models.CharField(max_length=20)
    deadline_time = models.DateTimeField(blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    files = models.ManyToManyField(Document, blank=True)
    groups = models.ForeignKey(StudentsGroup, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    SUBGROUP_CHOICE = (
        ('First', 'First'),
        ('Second', 'Second'),
        ('Both', 'Both')
    )
    WEEK_DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    )
    group_id = models.ForeignKey(StudentsGroup, on_delete=models.CASCADE)
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    subgroup = models.CharField(max_length=6, choices=SUBGROUP_CHOICE)
    week_day = models.CharField(max_length=9, choices=WEEK_DAY_CHOICES)
    time = models.IntegerField()


class Profile(models.Model):
    PERMISSION_CHOISE = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Admin', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_permission = models.CharField(max_length=7, choices=PERMISSION_CHOISE, default='Student')
    student_group = models.ForeignKey(StudentsGroup, blank=True, null=True, on_delete=models.SET_NULL)
    teacher_lesson = models.ManyToManyField(Lesson, blank=True)
    github = models.CharField(max_length=30, blank=True)
    numberphone = models.CharField(max_length=13, blank=True)
    img = models.ImageField(upload_to='profile_img', blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
