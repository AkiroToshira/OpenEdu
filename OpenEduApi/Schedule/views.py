from django.shortcuts import render

from rest_framework.response import Response

from rest_framework import permissions, viewsets

from itertools import groupby

from .models import Schedule

from Lessons.models import StudentGroupLesson

from Users.models import Group

from .serializers import ScheduleListSerializer


class ScheduleViewSet(viewsets.ViewSet):

    def list(self, request):

        user = request.user
        if user.profile.account_permission == 'Student':
            try:
                group = Group.objects.get(student=user)
            except:
                return Response('User have not group')
            lessons = StudentGroupLesson.objects.all().filter(group=group)
        elif user.profile.account_permission == 'Teacher':
            lessons = StudentGroupLesson.objects.all().filter(teacher=user)
        queryset = Schedule.objects.all().filter(lesson__in=lessons)
        serializer = ScheduleListSerializer(queryset, many=True)
        """"ПЕРЕПИСАТИ !!!"""
        output = {}
        for k, g in groupby(serializer.data, lambda x: x['week_day']):
            list = []
            for group in g:
                list.append(group)
            try:
                output[k].append(list[0])
            except:
                output[k] = list
        return Response(output)