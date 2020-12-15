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


class Institute(models.Model):
    name = models.CharField(max_length=30)


class Faculty(models.Model):
    name = models.CharField(max_length=30)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)


class Department(models.Model):
    name = models.CharField(max_length=30)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=10)
    departament = models.ForeignKey(Department, on_delete=models.CASCADE)
    curator = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    def get_lessons(self):
        lessons = StudentGroupLesson.objects.all().filter(student_group=self)
        return lessons

    def get_deadlines(self):
        deadline = GroupDeadline.objects.get(group=self)
        deadlines = deadline.get_all_deadlines()
        return deadlines


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

    def get_group(self):
        return self.group


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


class TeacherLesson(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)


@receiver(post_save, sender=Group)
def create_group_deadline(sender, instance, created, **kwargs):
    if created:
        new_group_deadline = GroupDeadline(group=instance)
        new_group_deadline.save()


class GroupDeadline(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def get_all_deadlines(self):
        deadlines = Deadlines.objects.all().filter(group_deadline=self)
        return deadlines


class Deadlines(models.Model):
    name = models.CharField(max_length=20)
    group_deadline = models.ForeignKey(GroupDeadline, on_delete=models.CASCADE)
    deadline_time = models.DateField(blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)


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
    TIME_CHOICE = (
        ('8:30 − 10:05', 1),
        ('10:20 − 11:55', 2),
        ('12:10 − 13:45', 3),
        ('14:15 − 15:50', 4),
        ('16:00 − 17:35', 5),
        ('17:40 − 19:15', 6),
        ('19:20 − 20:55', 7),
        ('21:00 − 22:35', 8),
    )
    student_group_lesson = models.ForeignKey(StudentGroupLesson, on_delete=models.CASCADE)
    subgroup = models.CharField(max_length=6, choices=SUBGROUP_CHOICE)
    week_day = models.CharField(max_length=9, choices=WEEK_DAY_CHOICES)
    time = models.CharField(max_length=13, choices=TIME_CHOICE)


class Profile(models.Model):
    PERMISSION_CHOISE = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Admin', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_permission = models.CharField(max_length=7, choices=PERMISSION_CHOISE, default='Student')
    github = models.CharField(max_length=30, blank=True)
    numberphone = models.CharField(max_length=13, blank=True)
    img = models.ImageField(upload_to='profile_img', blank=True)

    def get_student_group(self):
        group = StudentGroup.objects.get(student=self.user).get_group()
        return group

    def get_student_lessons(self):
        group = self.get_student_group()
        lessons = group.get_lessons()
        return lessons

    def get_student_deadlines(self):
        group = self.get_student_group()
        deadlines = group.get_deadlines()
        return deadlines

    def get_teacher_lessons(self):
        lessons = TeacherLesson.objects.all().filer(teacher=self.user)
        return lessons

    def get_teacher_lessons_groups(self):
        lessons = self.get_teacher_lessons()
        groups = StudentGroupLesson.objects.all().filter(lesson__in=lessons).distinct()
        return groups


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
