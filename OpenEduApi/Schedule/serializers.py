from rest_framework import serializers

from .models import Schedule, AdditionalInfoForScheduleDay

from Lessons.serializers import LessonListSerializer


class AdditionalInfoForScheduleDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = AdditionalInfoForScheduleDay
        fields = ('id', 'place', 'info')


class ScheduleListSerializer(serializers.ModelSerializer):

    addinfo = AdditionalInfoForScheduleDaySerializer(read_only=True)
    lesson = LessonListSerializer(read_only=True)

    class Meta:
        model = Schedule
        fields = ('id', 'lesson', 'subgroup', 'week_day', 'time', 'addinfo')
