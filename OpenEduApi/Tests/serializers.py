from rest_framework import serializers

from .models import QuestionSet


class QuestionSetListForStudent(serializers.ModelSerializer):

    class Meta:
        model = QuestionSet
        fields = ('title', 'visible', 'group')
