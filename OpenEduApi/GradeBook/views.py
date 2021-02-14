from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from .models import GradeBook, Grade

from Lessons.models import StudentGroupLesson

from .serializers import TeacherGradeBookSerializer, GradeSerializer, StudentLessonGradeBookSerializer

from Lessons.serializers import StudentGroupLessonSerializer


class TeacherGradeBookViewSet(viewsets.ViewSet):

    def grade_book_list(self, request):
        user = request.user
        lessons = StudentGroupLesson.get_user_lesson(user)
        serializer = StudentGroupLessonSerializer(lessons, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        lesson = StudentGroupLesson.objects.get(pk=pk)
        gradebook = lesson.gradebook
        serializer = TeacherGradeBookSerializer(gradebook)
        return Response(serializer.data)


class GradeViewSet(viewsets.ViewSet):

    def update(self, request):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            queryset = Grade.objects.all()
            grade = get_object_or_404(queryset, id=request.data.get('id'))
            serializer.update(grade, serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StudentGradeBookViewSet(viewsets.ViewSet):

    def list(self, request):
        user = request.user
        lessons = StudentGroupLesson.get_user_lesson(user)
        serializer = StudentLessonGradeBookSerializer(lessons, many=True)
        return Response(serializer.data)
