from django.db import models

from Lesson.models import Lesson

from Users.models import Group


class Deadlines(models.Model):
    name = models.CharField(max_length=20)
    deadline_time = models.DateTimeField(blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group)
