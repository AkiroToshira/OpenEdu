from rest_framework.response import Response
from rest_framework import permissions, viewsets
from django.shortcuts import get_object_or_404

from .models import User,Group,Profile

from .serializers import UserSerializer,GroupSerializer,GroupSerializer2

from rest_framework import status

class RegisterViewSet(viewsets.ViewSet):
    def create(self, request):
        user = User.objects.create(
                username=request.data.get('username'),
                email=request.data.get('email'),
                first_name=request.data.get('firstName'),
                last_name=request.data.get('lastName')
            )
        user.set_password(str(request.data.get('password')))
        user.save()
        return Response({"status":"success","response":"User Successfully Created"}, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def retrieve(self, request, pk=None):
        """"Вивід інформації про користувача"""
        queryset = User.objects.all()
        lesson = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(lesson)
        return Response(serializer.data)


class UserViewSetReact(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def retrieve(self, request):
        user = request.user
        return Response({'id': user.id, 'perm': user.profile.account_permission})

class GroupViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request):
        """Створення групи"""
        serializer = GroupSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        """Видалення групи за айді"""
        serializer = GroupSerializer2(data=request.data)
        temp = Group.objects.get(id=pk)
        if serializer.is_valid():
            temp.delete()
            return Response('Group {} deleted successfully'.format(serializer.data))
        else:
            return Response(serializer.errors)

    def list(self,request):
        """Вивід списку груп"""
        queryset = Group.objects.all()
        serializer = GroupSerializer(queryset, many=True)

        return Response(serializer.data)

    def add_student(self, request, pk):
        """Додавання студента(id в body) до групи(id в url)"""
        queryset = Group.objects.all()
        group = get_object_or_404(queryset,pk=pk)
        group.student.add(request.data.get('id'))
        queryset2 = Profile.objects.all()
        user = get_object_or_404(queryset2, pk=request.data.get('id'))
        group.save()

        return Response('Student {} has been successfully added to group {}'.format(user.user,group.name))

    def remove_student(self,request, pk):
        """Видалення студента(id в body) з групи(id в url)"""
        queryset = Group.objects.all()
        group = get_object_or_404(queryset, pk=pk)
        group.student.remove(request.data.get('id'))
        queryset2 = Profile.objects.all()
        user = get_object_or_404(queryset2, pk=request.data.get('id'))
        group.save()

        return Response('Student {} has been successfully removed from the group {}'.format(user.user, group.name))