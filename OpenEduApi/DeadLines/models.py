from django.db import models

from Lesson.models import StudentGroupLesson


class Deadlines(models.Model):
    name = models.CharField(max_length=20)
    deadline_time = models.DateTimeField(blank=True)
    lesson = models.ForeignKey(StudentGroupLesson, on_delete=models.CASCADE)

