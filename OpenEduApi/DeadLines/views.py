from rest_framework.response import Response
from rest_framework import viewsets

from .models import Deadlines

from Lessons.models import StudentGroupLesson

from .serializers import DeadlinesSerializer


class DeadlinesViewSet(viewsets.ViewSet):

    def list(self, request):
        user = request.user
        lessons = StudentGroupLesson.get_user_lesson(user)
        queryset = Deadlines.objects.all().filter(lesson__in=lessons)
        serializer = DeadlinesSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DeadlinesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def update(self, request):
        serializer = DeadlinesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(
                Deadlines.objects.get(id=request.data.get('id')), serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
