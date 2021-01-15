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


class TeacherStudentGroupLesson(models.Model):
    """"Викладач може керувати данними предметом, який привязаний до певної групи"""
    student_group_lesson = models.ForeignKey(StudentGroupLesson, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
