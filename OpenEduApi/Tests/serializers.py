from rest_framework import serializers

from .models import QuestionSet, Question, Answer, UserAnswer


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
        fields = ('id', 'title', 'open_since', 'open_until', 'limit', 'questions')


class UserAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAnswer
        fields = ('id', 'user', 'questions_set', 'score')


class QuestionSetListForStudentSerializer(serializers.ModelSerializer):
    user_answer = UserAnswerSerializer(many=True)

    class Meta:
        model = QuestionSet
        fields = ('id', 'title', 'open_since', 'open_until', 'limit', 'user_answer')
