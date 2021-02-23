from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from Lessons.models import StudentGroupLesson

from .serializers import CountGradeBookSerializer


class CountGradeBookViewSet(viewsets.ViewSet):

    def simple_count(self, request, pk=None):
        lessons = StudentGroupLesson.objects.all()
        lesson = get_object_or_404(lessons, pk=pk)
        gradebook = lesson.gradebook
        serializer = CountGradeBookSerializer(gradebook)
        return Response(serializer.data)
