from rest_framework import serializers

from .models import Deadlines

from Lessons.models import StudentGroupLesson

from Lessons.serializers import LessonSerializer


class DeadlinesSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(StudentGroupLesson.get_lesson)

    class Meta:
        model = Deadlines
        fields = "__all__"


class DeadlinesCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deadlines
        fields = ('name', 'description', 'deadline_time', 'lesson', 'type')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description',
            instance.description)
        instance.deadline_time = validated_data.get(
            'deadline_time',
            instance.deadline_time)
        instance.save()
        return instance
