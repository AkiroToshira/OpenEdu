from rest_framework.response import Response
from rest_framework import permissions, viewsets
from django.shortcuts import get_object_or_404

from .serializers import *

from Users.models import Group,Profile
from .models import *


class StudentLessonListViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def create(self,request):
        """Створення предмету"""
        serializer = LessonDetailSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def update(self, request,pk):
        """Редагування предмету за айді"""
        serializer = LessonDetailSerializer2(data=request.data)
        temp = Lesson.objects.get(id=pk)
        if serializer.is_valid():
            serializer.update(temp, serializer.data)
            return Response('Lesson updated successfully. New one {}'.format(serializer.data))
        else:
            return Response(serializer.errors)


    def delete(self, request,pk):
        """Видалення предмету за айді"""
        serializer = LessonDetailSerializer2(data=request.data)
        temp = Lesson.objects.get(id=pk)
        if serializer.is_valid():
            temp.delete()
            return Response('Lesson {} deleted successfully'.format(serializer.data))
        else:
            return Response(serializer.errors)

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
        serializer = ChapterUpdateSerializer(data=request.data)
        if serializer.is_valid():
            queryset = Chapter.objects.all()
            chapter = get_object_or_404(queryset, pk=pk)
            serializer.update(chapter, serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

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

class AdminViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def add_moderator(self, request, pk):
        """Додавання модераторів(id в body) до предмету(id в url)"""
        queryset = Lesson.objects.all()
        lesson = get_object_or_404(queryset,pk=pk)
        lesson.lesson_moderator.add(request.data.get('id'))
        queryset2 = Profile.objects.all()
        user = get_object_or_404(queryset2, pk=request.data.get('id'))
        lesson.save()

        return Response('Moderator {} has been successfully added to lesson {}'.format(user.user,lesson.name))

    def remove_moderator(self,request, pk):
        """Видалення модератора(id в body) від предмету(id в url)"""
        queryset = Lesson.objects.all()
        lesson = get_object_or_404(queryset, pk=pk)
        lesson.lesson_moderator.remove(request.data.get('id'))
        queryset2 = Profile.objects.all()
        user = get_object_or_404(queryset2, pk=request.data.get('id'))
        lesson.save()

        return Response('Moderator {} has been successfully removed from the lesson {}'.format(user.user, lesson.name))

"""
    def add_group(self, request, pk=None):
        Додавання групи(id в body) до предмету(id в url)
        queryset = Lesson.objects.all()
        lesson1 = get_object_or_404(queryset,pk=pk)

        queryset2 = Group.objects.all()
        group = get_object_or_404(queryset2, pk=request.data.get('id'))

        lesson = StudentGroupLesson()
        lesson.group= group
        lesson.lesson=lesson1
        lesson.save()

        return Response('Group {} has been successfully added to lesson {}'.format(group.name,lesson1.name))


    def remove_group(self,request, pk=None):
        Видалення групи(id в body) від предмету(id в url)
        queryset = Lesson.objects.all()
        lesson1 = get_object_or_404(queryset, pk=pk)

        queryset2 = Group.objects.all()
        group = get_object_or_404(queryset2, pk=request.data.get('id'))

        lesson1.
        .remove(request.data.get('id'))
        lesson = StudentGroupLesson()
        lesson.group = group
        lesson.lesson = lesson1
        lesson.save()

        return Response('Group {} has been successfully deleted from lesson {}'.format(group.name, lesson1.name))
"""