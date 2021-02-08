from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Institute(models.Model):
    """"Інститут"""
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    """"Факультет"""
    name = models.CharField(max_length=30)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Department(models.Model):
    """"Кафедра"""
    name = models.CharField(max_length=30)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Group(models.Model):
    """"Група студентів"""
    name = models.CharField(max_length=10)
    departament = models.ForeignKey(Department, on_delete=models.CASCADE)
    curator = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name='curatorial_group')
    year = models.PositiveIntegerField(default=1)
    student = models.ManyToManyField(User, related_name='Student_group', blank=True)

    def get_all_students(self):
        return User.objects.all().filter(Student_group=self)

    def __str__(self):
        return self.name


class Profile(models.Model):
    """"Доповнення моделі User, за дпопомогою каскадного створення додаткової таблиці"""
    PERMISSION_CHOISE = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Admin', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    middle_name = models.CharField(max_length=150, blank=True)
    account_permission = models.CharField(max_length=7, choices=PERMISSION_CHOISE, default='Student')
    numberphone = models.CharField(max_length=13, blank=True)
    credit_book_number = models.CharField(max_length=8, blank=True)
    img = models.ImageField(upload_to='profile_img', blank=True, default='profile_img/profile_photo.jpg')

    def get_full_name(self):
        return self.middle_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """"Створення Profile після створення User"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """"Зберігання Profile"""
    instance.profile.save()
