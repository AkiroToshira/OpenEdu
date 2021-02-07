from rest_framework import serializers

from .models import Deadlines

from Lessons.models import StudentGroupLesson


class DeadlinesSerializer(serializers.ModelSerializer):
    lesson = StudentGroupLesson.get_lesson

    class Meta:
        model = Deadlines
        fields = "__all__"

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
