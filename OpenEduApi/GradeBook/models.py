from django.db import models

from Lessons.models import StudentGroupLesson

from django.contrib.auth.models import User


class GradeBook(models.Model):
    group = models.ForeignKey(StudentGroupLesson, on_delete=models.CASCADE)


class BookColumn(models.Model):
    date = models.DateField(blank=False)
    gradebook = models.ForeignKey(GradeBook, blank=True, on_delete=models.CASCADE)


class Grade(models.Model):
    date = models.ForeignKey(BookColumn, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=3, default='')
