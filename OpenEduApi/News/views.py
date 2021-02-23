from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions

from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer, ArticleSerializer


class ArticleViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        """"Вивід списку новин"""
        queryset = Article.objects.all()
        serializer = ArticleListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """"Детальний вивід новини"""
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    def post(self, request):
        article = request.data.get('article')

        # Create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})