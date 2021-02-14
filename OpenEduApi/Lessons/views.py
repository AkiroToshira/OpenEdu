from rest_framework.response import Response
from rest_framework import permissions, viewsets
from django.shortcuts import get_object_or_404

from .serializers import *

from Users.models import Group


class StudentLessonListViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        """"Вивід списку предметів студента"""
        user = request.user
        try:
            group = Group.objects.get(student=user)
        except:
            return Response('User have not group')
        queryset = StudentGroupLesson.objects.all().filter(group=group)
        serializer = LessonSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """"Детальний вивід інформації про предмет для студента"""
        lesson_queryset = Lesson.objects.all()
        lesson = get_object_or_404(lesson_queryset, pk=pk)
        lesson_data = LessonDetailSerializer(lesson)
        return Response(lesson_data.data)


class TeacherLessonListViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        """"Вивід списку предметів викладача"""
        user = request.user
        queryset = Lesson.objects.all().filter(lesson_moderator=user)
        serializer = TeacherLessonListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """"Детальний вивід інформації про предмет для викладача"""
        queryset = Lesson.objects.all()
        lesson = get_object_or_404(queryset, pk=pk)
        lesson_serializer = LessonDetailSerializer(lesson)
        return Response(lesson_serializer.data)


class ChapterViewSet(viewsets.ViewSet):

    def create(self, request):
        user = request.user
        chapter_serializer = ChapterCreateSerializer(data=request.data)
        if chapter_serializer.is_valid():
            new_chapter = chapter_serializer.save()
            if request.data.get('file'):
                for i in request.data.getlist('file'):
                    document_serializer = DocumentCreateSerializer(data=
                                                                   {'user': user.id,
                                                                    'file': i,
                                                                    'chapter': new_chapter.id})
                    if document_serializer.is_valid():
                        document_serializer.save()
                    else:
                        return Response(document_serializer.errors)
            return Response(ChapterSerializer(new_chapter).data)
        else:
            return Response(chapter_serializer.errors)

    def update(self, request, pk=None):
        serializer = ChapterCreateSerializer(data=request.data)
        if serializer.is_valid():
            queryset = Chapter.objects.all()
            chapter = get_object_or_404(queryset, pk=pk)
            serializer.update(chapter, serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializers.errors)

    def delete(self, request, pk=None):
        queryset = Chapter.objects.all()
        chapter = get_object_or_404(queryset, pk=pk)
        chapter.delete()
        return Response('Deleted')


class DocumentViewSet(viewsets.ViewSet):

    def list(self, request):
        user = request.user
        queryset = Document.objects.all().filter(user=user)
        serializer = DocumentCreateSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = request.user
        file = request.data.get('file')
        chapter = request.data.get('chapter')
        document_serializer = DocumentCreateSerializer(data=
                                                       {'user': user.id,
                                                        'file': file,
                                                        'chapter': chapter})
        if document_serializer.is_valid():
            document_serializer.save()
        else:
            return Response(document_serializer.errors)

    def delete(self, request):
        queryset = Document.objects.all()
        document = get_object_or_404(queryset, pk=request.data.get('id'))
        document.delete()
        return Response('Deleted')
