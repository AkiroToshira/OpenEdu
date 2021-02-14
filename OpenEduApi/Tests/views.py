from rest_framework.response import Response
from rest_framework import permissions, viewsets
from django.shortcuts import get_object_or_404

from Users.models import Group

from .models import QuestionSet, Answer, UserAnswer

from .serializers import (QuestionSetListForStudentSerializer,
                          DetailQuestionSetListForStudentSerializer,
                          UserAnswerSerializer)


class StudentTestViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, pk=None):
        """"Вивід тестів доступних для учня з певного предмету"""
        user = request.user
        try:
            group = Group.objects.get(student=user)
        except:
            return Response('User have not group')
        queryset = QuestionSet.objects.all().filter(group=group, lesson=pk, visible=True)
        serializer = QuestionSetListForStudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = QuestionSet.objects.all()
        questionset = get_object_or_404(queryset, pk=pk)
        serializer = DetailQuestionSetListForStudentSerializer(questionset)
        return Response(serializer.data)

    def count(self, request, pk=None):
        answers = request.data.get('answers')
        answers = answers.split(' ')
        answers = Answer.objects.all().filter(id__in=answers)
        mark = 0
        for i in answers:
            mark += i.mark
        user = request.user
        serializer = UserAnswerSerializer(data={'user': user.id,
                                                'questions_set': pk, 'score': mark})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
