from django.db import models

from Lessons.models import Lesson, StudentGroupLesson

from Users.models import Group


class Schedule(models.Model):
    SUBGROUP_CHOICE = (
        ('First', 'F'),
        ('Second', 'S'),
        ('Both', 'B')
    )
    WEEK_DAY_CHOICES = (
        ('Monday', 'M'),
        ('Tuesday', 'T'),
        ('Wednesday', 'W'),
        ('Thursday', 'T'),
        ('Friday', 'F'),
    )
    TIME_CHOICE = (
        ('8:30 − 10:05', '1'),
        ('10:20 − 11:55', '2'),
        ('12:10 − 13:45', '3'),
        ('14:15 − 15:50', '4'),
        ('16:00 − 17:35', '5'),
        ('17:40 − 19:15', '6'),
        ('19:20 − 20:55', '7'),
        ('21:00 − 22:35', '8'),
    )
#    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='schedules')
    lesson = models.ForeignKey(StudentGroupLesson, on_delete=models.CASCADE)
    subgroup = models.CharField(max_length=6, choices=SUBGROUP_CHOICE)
    week_day = models.CharField(max_length=9, choices=WEEK_DAY_CHOICES)
    time = models.CharField(max_length=13, choices=TIME_CHOICE)


class AdditionalInfoForScheduleDay(models.Model):
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE, related_name='addinfo')
    place = models.CharField(max_length=30, blank=True)
    info = models.CharField(max_length=50, blank=True)
