from rest_framework import serializers

from .models import *

from Users.serializers import ShortUserInfoSerializer

from Lessons.serializers import TeacherStudentGroupListSerializer, TeacherLessonListSerializer

from Lessons.models import StudentGroupLesson


class GradeSerializer(serializers.ModelSerializer):

    user = ShortUserInfoSerializer(read_only=True)

    class Meta:
        model = Grade
        fields = ('id', 'user', 'value')

    def update(self, instance, validated_data):
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance


class ColumnsGradeBookSerializer(serializers.ModelSerializer):

    grades = GradeSerializer(many=True, read_only=True)

    class Meta:
        model = BookColumn
        fields = ('date', 'grades')


class TeacherGradeBookSerializer(serializers.ModelSerializer):

    columns = ColumnsGradeBookSerializer(many=True, read_only=True)
    group = TeacherStudentGroupListSerializer(read_only=True)

    class Meta:
        model = GradeBook
        fields = ('id', 'group', 'columns')


class StudentGradeBookSerializer(serializers.ModelSerializer):

    columns = ColumnsGradeBookSerializer(many=True, read_only=True)

    class Meta:
        model = GradeBook
        fields = ('columns',)


class StudentLessonGradeBookSerializer(serializers.ModelSerializer):

    gradebook = StudentGradeBookSerializer(read_only=True)
    lesson = TeacherLessonListSerializer(read_only=True)
    class Meta:
        model = StudentGroupLesson
        fields = ('lesson', 'gradebook',)
