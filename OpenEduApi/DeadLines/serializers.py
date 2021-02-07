from rest_framework import serializers

from .models import Deadlines

from Lessons.models import StudentGroupLesson


class DeadlinesSerializer(serializers.ModelSerializer):
    lesson = StudentGroupLesson.get_lesson

    class Meta:
        model = Deadlines
        fields = ('name', 'description', 'deadline_time', 'lesson', 'type')
