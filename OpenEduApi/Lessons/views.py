from rest_framework.response import Response
from rest_framework import permissions, viewsets

from .models import StudentGroupLesson, Lesson, TeacherLesson

from .serializers import LessonListSerializer, StudentLessonListSerializer, TeacherLessonListSerializer


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


class TeacherLessonListViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        """"Вивід списку предметів викладача"""
        user = request.user
        queryset = TeacherLesson.objects.all().filter(teacher=user)
        serializer = TeacherLessonListSerializer(queryset, many=True)
        return Response(serializer.data)
