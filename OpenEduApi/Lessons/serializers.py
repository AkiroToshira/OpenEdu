from rest_framework import serializers

from .models import *


class LessonListSerializer(serializers.ModelSerializer):
    """"Список предметів"""

    class Meta:
        model = Lesson
        fields = ('id', 'name')


class LessonDetailSerializer(serializers.ModelSerializer):
    """"Інформація про предмет"""

    class Meta:
        model = Lesson
        fields = '__all__'


class StudentLessonListSerializer(serializers.ModelSerializer):
    """"Вивід предметів учня з списку StudentGroupLesson"""

    lesson = LessonListSerializer(read_only=True)

    class Meta:
        model = StudentGroupLesson
        fields = ('lesson',)


class TeacherLessonListSerializer(serializers.ModelSerializer):
    """"Вивід предметів вчителя з списку TeacherLesson"""

    lesson = LessonListSerializer(read_only=True)

    class Meta:
        model = TeacherLesson
        fields = ('lesson',)
