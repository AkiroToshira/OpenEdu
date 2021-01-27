from rest_framework import serializers

from .models import *
from Users.models import Group
from Users.serializers import ShortUserInfoSerializer


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


class LessonDetailSerializer(serializers.ModelSerializer):
    """"Інформація про предмет"""
    chapters = ChapterSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'chapters']


class StudentLessonListSerializer(serializers.ModelSerializer):
    """"Вивід предметів учня з списку StudentGroupLesson"""

    lesson = LessonListSerializer(read_only=True)

    class Meta:
        model = StudentGroupLesson
        fields = ('lesson',)


#class TeacherLessonListSerializer(serializers.ModelSerializer):
#    """"Вивід предметів вчителя з списку TeacherLesson"""
#
#    lesson = LessonListSerializer(read_only=True)
#
#    class Meta:
#        model = TeacherLesson
#        fields = ('lesson',)


class GroupSerializer(serializers.ModelSerializer):
    """"Вивіл ід і імен групи"""

    class Meta:
        model = Group

        fields = ('id', 'name')


class TeacherStudentGroupListSerializer(serializers.ModelSerializer):
    """"Вивід списоку груп, у яких веде пару вилкладач. З моделі StudentGroupLesson"""

    group = GroupSerializer()

    class Meta:
        model = StudentGroupLesson

        fields = ('group',)


class TeacherLessonSerializer(serializers.ModelSerializer):
    """"Вивід інформації про викладача з StudentGroupLesson"""
    teachers = ShortUserInfoSerializer(read_only=True, many=True)

    class Meta:
        model = StudentGroupLesson

        fields = ('teachers',)
