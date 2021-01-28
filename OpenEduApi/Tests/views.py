from rest_framework.response import Response

from rest_framework import permissions, viewsets

from User.models import Group

from .models import QuestionSet

from .serializers import QuestionSetListForStudent


class StudentTestViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, pk=None):
        """"Вивід тестів доступних для учня з певного предмету"""
        user = request.user
        try:
            group = Group.objects.get(student=user)
        except:
            return Response('User have not group')
        queryset = QuestionSet.objects.all().filter(group=group, lesson=pk)
        serializer = QuestionSetListForStudent(queryset, many=True)
        return Response(serializer.data)
