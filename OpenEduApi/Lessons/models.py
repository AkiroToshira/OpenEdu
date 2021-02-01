from django.db import models
from django.contrib.auth.models import User
from Users.models import Group


class Lesson(models.Model):
    """"Предмет"""
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=30, blank=True)
    lesson_moderator = models.ManyToManyField(User, related_name='LessonModerator', blank=True)


class StudentGroupLesson(models.Model):
    """"Групи і викладачі прив'язані до предмету"""
    TYPE_CHOICE = (
        ('Lessons', 'L'),
        ('Practical ', 'P')
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='GroupLesson', on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, related_name='TeacherGroup', on_delete=models.CASCADE)


class Lecture(models.Model):
    """Лекції які йдуть разом"""
    lesson = models.ManyToManyField(StudentGroupLesson, related_name='Lecture')


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
