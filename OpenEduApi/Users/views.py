from rest_framework.response import Response
from rest_framework import permissions, viewsets
from django.shortcuts import get_object_or_404

from .models import User

from .serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def retrieve(self, request, pk=None):
        """"Вивід інформації про користувача"""
        queryset = User.objects.all()
        lesson = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(lesson)
        return Response(serializer.data)
