from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Articles(models.Model):
    articles_data = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=200)
    img = models.ImageField(upload_to='article', blank=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    description = models.CharField(max_length=20, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class Lesson(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=30, blank=True)
    files = models.ManyToManyField(Document, blank=True)

    def __str__(self):
        return self.name


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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_group = models.ForeignKey(StudentsGroup, blank=True, null=True, on_delete=models.SET_NULL)
    github = models.CharField(max_length=30, blank=True)
    numberphone = models.CharField(max_length=13, blank=True)
    img = models.ImageField(upload_to='profile_img', blank=True)

    def save(self):
        super().save()
        img = Image.open(self.img.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.img.path)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

