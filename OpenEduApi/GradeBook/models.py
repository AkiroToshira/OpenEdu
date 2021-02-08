from django.db import models

from Lessons.models import StudentGroupLesson

from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class GradeBook(models.Model):
    group = models.OneToOneField(StudentGroupLesson, on_delete=models.CASCADE, related_name='gradebook')


class BookColumn(models.Model):
    date = models.DateField(blank=False)
    gradebook = models.ForeignKey(GradeBook, blank=True, on_delete=models.CASCADE, related_name='columns')


class Grade(models.Model):
    date = models.ForeignKey(BookColumn, on_delete=models.CASCADE, related_name='grades')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=3, default='')


@receiver(post_save, sender=BookColumn)
def create_grade(sender, instance, created, **kwargs):
    if created:
        group = instance.gradebook.group.group
        students = group.get_all_students()
        for student in students:
            new_grade = Grade(date=instance, user=student)
            new_grade.save()
