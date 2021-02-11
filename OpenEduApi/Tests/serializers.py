from rest_framework import serializers

from .models import QuestionSet, Question, Answer


class AnswerListForStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'text', 'img')


class QuestionsListForStudentSerializer(serializers.ModelSerializer):
    answers = AnswerListForStudentSerializer(many=True)

    class Meta:
        model = Question
        fields = ('text', 'img', 'answers')


class DetailQuestionSetListForStudentSerializer(serializers.ModelSerializer):
    questions = QuestionsListForStudentSerializer(many=True)

    class Meta:
        model = QuestionSet
        fields = ('id', 'title', 'open_since', 'open_until', 'limit', 'type', 'questions')


class QuestionSetListForStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionSet
        fields = ('id', 'title', 'open_since', 'open_until', 'limit', 'type')
