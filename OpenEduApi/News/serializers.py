from rest_framework import serializers

from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    """Список новин"""

    class Meta:
        model = Article
        fields = ('id', 'name', 'creation_date', 'mini_description', 'img')


class ArticleDetailSerializer(serializers.ModelSerializer):
    """"Детальний опис новини"""

    class Meta:
        model = Article
        fields = ('id', 'name', 'creation_date', 'description', 'img')

class ArticleSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=120)
    description = serializers.CharField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)