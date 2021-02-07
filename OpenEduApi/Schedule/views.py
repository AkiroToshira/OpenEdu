from rest_framework.response import Response

from rest_framework import viewsets

from itertools import groupby

from .models import Schedule

from Lessons.models import StudentGroupLesson, LessonTeacher

from .serializers import ScheduleListSerializer


class ScheduleViewSet(viewsets.ViewSet):

    def list(self, request):
        user = request.user
        lessons = StudentGroupLesson.get_user_lesson(user)
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
