from rest_framework.response import Response
from rest_framework import permissions, viewsets
from django.shortcuts import get_object_or_404

from .serializers import *

from Users.models import Group


class StudentLessonListViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        """"Вивід списку предметів студента"""
        user = request.user
        try:
            group = Group.objects.get(student=user)
        except:
            return Response('User have not group')
        queryset = StudentGroupLesson.objects.all().filter(group=group)
        serializer = LessonSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """"Детальний вивід інформації про предмет для студента"""
        lesson_queryset = Lesson.objects.all()
        lesson = get_object_or_404(lesson_queryset, pk=pk)
        lesson_data = LessonDetailSerializer(lesson)
        return Response(lesson_data.data)


class TeacherLessonListViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        """"Вивід списку предметів викладача"""
        user = request.user
        queryset = Lesson.objects.all().filter(lesson_moderator=user)
        serializer = TeacherLessonListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """"Детальний вивід інформації про предмет для викладача"""
        queryset = Lesson.objects.all()
        lesson = get_object_or_404(queryset, pk=pk)
        lesson_serializer = LessonDetailSerializer(lesson)
        user = request.user
        queryset = StudentGroupLesson.objects.all().filter(lesson=pk, teachers=user)
        groups_serializer = TeacherStudentGroupListSerializer(queryset, many=True)
        return Response({'lesson_data': lesson_serializer.data, 'groups': groups_serializer.data})
