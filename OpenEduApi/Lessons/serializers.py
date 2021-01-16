from rest_framework import serializers

from .models import *


class LessonListSerializer(serializers.ModelSerializer):
    """"Список предметів"""

    class Meta:
        model = Lesson
        fields = ('id', 'name')


class DocumentSerializer(serializers.ModelSerializer):
    """"Вивід фалів розділу"""
    class Meta:
        model = Document
        fields = ('file',)


class ChapterSerializer(serializers.ModelSerializer):
    """"Вивід розділів предмету"""
    documents = DocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = ['name', 'description', 'documents']


class StudentLessonDetailSerializer(serializers.ModelSerializer):
    """"Інформація про предмет для учня"""
    chapters = ChapterSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ['name', 'description', 'chapters']


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
