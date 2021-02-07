from django.db import models

from Lessons.models import StudentGroupLesson


class Deadlines(models.Model):
    TYPE_CHOICE = (
        ('Lab', 'Lab'),
        ('Test', 'Test'),
        ('Task', 'Task')
    )
    type = models.CharField(choices=TYPE_CHOICE, max_length=4, default='Task')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    deadline_time = models.DateField(blank=True)
    lesson = models.ForeignKey(StudentGroupLesson, on_delete=models.CASCADE)

