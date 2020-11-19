from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Articles(models.Model):
    articles_data = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=200)
    img = models.ImageField(upload_to='article')

    def __str__(self):
        return self.name


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Lesson(models.Model):
    name = models.CharField(max_length=30)
    files = models.ManyToManyField(Document)

    def __str__(self):
        return self.name


class StudentsGroup(models.Model):
    name = models.CharField(max_length=10)
    lessons = models.ManyToManyField(Lesson)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_group = models.ForeignKey(StudentsGroup, blank=True, null=True, on_delete=models.SET_NULL)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

