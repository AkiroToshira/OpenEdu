from rest_framework.response import Response
from rest_framework import permissions, viewsets
from django.shortcuts import get_object_or_404

from .models import StudentGroupLesson, Lesson, TeacherLesson

from .serializers import *


class LessonViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        """"Вивід списку предметів"""
        queryset = Lesson.objects.all()
        serializer = LessonListSerializer(queryset, many=True)
        return Response(serializer.data)


class StudentLessonListViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        """"Вивід списку предметів студента"""
        user = request.user
        queryset = StudentGroupLesson.objects.all().filter(group=user.profile.group)
        serializer = StudentLessonListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """"Детальний вивід інформації про предмет для студента"""
        lesson_queryset = Lesson.objects.all()
        lesson = get_object_or_404(lesson_queryset, pk=pk)
        lesson_data = LessonDetailSerializer(lesson)
        user = request.user
        teachers_queryset = StudentGroupLesson.objects.all()
        teachers = get_object_or_404(teachers_queryset, lesson=lesson, group=user.profile.group)
        teacher_data = TeacherLessonSerializer(teachers)
        return Response({'lesson_data': lesson_data.data, 'teachers': teacher_data.data})


class TeacherLessonListViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        """"Вивід списку предметів викладача"""
        user = request.user
        queryset = TeacherLesson.objects.all().filter(teacher=user)
        serializer = TeacherLessonListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """"Детальний вівід інформації про предмет для викладача"""
        queryset = Lesson.objects.all()
        lesson = get_object_or_404(queryset, pk=pk)
        lesson_serializer = LessonDetailSerializer(lesson)
        user = request.user
        queryset = StudentGroupLesson.objects.all().filter(lesson=pk, teachers=user)
        groups_serializer = TeacherStudentGroupListSerializer(queryset, many=True)
        return Response({'lesson_data': lesson_serializer.data, 'groups': groups_serializer.data})

