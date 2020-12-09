from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
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
    group_id = models.ForeignKey(StudentsGroup, on_delete=models.CASCADE)
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    subgroup = models.CharField(max_length=6, choices=SUBGROUP_CHOICE)
    week_day = models.CharField(max_length=9, choices=WEEK_DAY_CHOICES)
    time =models.CharField(max_length=13, choices=TIME_CHOICE)


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