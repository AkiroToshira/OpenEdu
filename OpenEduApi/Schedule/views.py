from django.shortcuts import render

from rest_framework.response import Response

from rest_framework import permissions, viewsets

from itertools import groupby

from .models import Schedule

from Users.models import Group

from .serializers import ScheduleListSerializer


class ScheduleViewSet(viewsets.ViewSet):

    def list(self, request):

        user = request.user
        try:
            group = Group.objects.get(student=user)
        except:
            return Response('User have not group')
        queryset = group.schedules.all()
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
