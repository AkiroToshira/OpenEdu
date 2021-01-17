from django.db import models
from django.contrib.auth.models import User
from Users.models import Group


class Lesson(models.Model):
    """"Предмет"""
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=30, blank=True)


class TeacherLesson(models.Model):
    """"Викладачі, які можуть керувати певним предметом"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)


class StudentGroupLesson(models.Model):
    """"Група прив'язана до певного предмету"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(User)


class Chapter(models.Model):
    """"Поділ розділів предмету"""
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=30, blank=True)
    lesson = models.ForeignKey(Lesson, related_name='chapters', on_delete=models.CASCADE)


class Document(models.Model):
    """"Файли прикріплені до певного розділу"""
    chapter = models.ForeignKey(Chapter, related_name='documents', on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


