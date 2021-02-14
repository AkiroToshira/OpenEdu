from django.db import models

from Lessons.models import Lesson
from Users.models import Group
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class QuestionSet(models.Model):
    """"До цього об'єднюються всі питання"""
    LIMIT_CHOICES = (
        ('No', 'NoL'),
        ('Time', 'TiL'),
        ('Try', 'TrL'),
        ('Try&Time', 'TiTrL')
    )
    title = models.CharField(max_length=30, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    group = models.ManyToManyField(Group)
    visible = models.BooleanField(default=True)
    open_since = models.DateField(blank=True, null=True)
    open_until = models.DateTimeField(blank=True, null=True)
    limit = models.CharField(max_length=8, choices=LIMIT_CHOICES)
    time_limit = models.TimeField(blank=True, null=True)


class Question(models.Model):
    """"Питання"""
    question_set = models.ForeignKey(QuestionSet, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=60, blank=True)
    img = models.ImageField(upload_to='question', blank=True)
    max_mark = models.PositiveIntegerField(default=0)

    def max_mark_count(self):
        questions = self.answers.all()
        max_mark = 0
        for i in questions:
            max_mark += i.mark
        self.max_mark = max_mark
        self.save()


class Answer(models.Model):
    """"Відповідь"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    mark = models.PositiveIntegerField(default=0)
    text = models.CharField(max_length=60, blank=True)
    img = models.ImageField(upload_to='answer', blank=True)


@receiver(post_save, sender=Answer)
def max_mark_counting(sender, instance, created, **kwargs):
    question_set = instance.question
    question_set.max_mark_count()


class UserAnswer(models.Model):
    """Результати користувача"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions_set = models.ForeignKey(QuestionSet, on_delete=models.CASCADE, related_name='user_answer')
    score = models.CharField(max_length=3)

