from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from .models import Deadlines

from Lessons.models import StudentGroupLesson

from .serializers import DeadlinesSerializer, DeadlinesCreateSerializer


class DeadlinesViewSet(viewsets.ViewSet):

    def list(self, request):
        user = request.user
        lessons = StudentGroupLesson.get_user_lesson(user)
        queryset = Deadlines.objects.all().filter(lesson__in=lessons)
        serializer = DeadlinesSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DeadlinesCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def update(self, request):
        serializer = DeadlinesCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(
                Deadlines.objects.get(id=request.data.get('id')), serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request):
        queryset = Deadlines.objects.all()
        deadline = get_object_or_404(queryset, pk=request.data.get('id'))
        deadline.delete()
        return Response('Deleted')
