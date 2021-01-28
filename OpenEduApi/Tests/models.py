from django.db import models

from Lessons.models import Lesson
from Users.models import Group
from django.contrib.auth.models import User


class QuestionSet(models.Model):
    """"До цього об'єднюються всі питання"""
    LIMIT_CHOICES = (
        ('NoL', 'No'),
        ('TiL', 'Time'),
        ('TrL', 'Try'),
        ('TiTrL', 'Try&Time')
    )
    TYPE_CHOICES = (
        ('O', 'One'),
        ('T', 'Tickets'),
        ('S', 'Set')
    )
    title = models.CharField(max_length=30, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    group = models.ManyToManyField(Group)
    visible = models.BooleanField(default=True)
    open_since = models.DateField(blank=True)
    open_until = models.DateTimeField(blank=True)
    limit = models.CharField(max_length=8, choices=LIMIT_CHOICES)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)


class Question(models.Model):
    """"Питання"""
    text = models.CharField(max_length=60, blank=True)
    img = models.ImageField(upload_to='question', blank=True)


class Answer(models.Model):
    """"Відповідь"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField(default=0)
    text = models.CharField(max_length=60, blank=True)
    img = models.ImageField(upload_to='answer', blank=True)


class UserAnswer(models.Model):
    """Результати користувача"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions_set = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)

