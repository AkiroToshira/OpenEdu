from rest_framework import serializers

from GradeBook.models import GradeBook, Grade, BookColumn

from Users.models import User

from GradeBook.serializers import ExamGradeSerializer

from Lessons.serializers import TeacherStudentGroupListSerializer


class UserInfo(serializers.ModelSerializer):
    middle_name = serializers.SerializerMethodField('middle_name_foo')
    credit_book_number = serializers.SerializerMethodField('get_credit_book_number')

    def get_credit_book_number(self, user):
        return user.profile.credit_book_number

    def middle_name_foo(self, user):
        return user.profile.middle_name

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'credit_book_number')


class GradeSerializer(serializers.ModelSerializer):

    user = UserInfo(read_only=True)

    class Meta:
        model = Grade
        fields = ('id', 'user', 'value')


class ColumnsGradeBookSerializer(serializers.ModelSerializer):

    grades = GradeSerializer(many=True, read_only=True)

    class Meta:
        model = BookColumn
        fields = ('date', 'grades')


class CountGradeBookSerializer(serializers.ModelSerializer):
    columns = ColumnsGradeBookSerializer(many=True, read_only=True)
    group = TeacherStudentGroupListSerializer(read_only=True)
    exam = ExamGradeSerializer(many=True, read_only=True)
    lesson = serializers.SerializerMethodField('get_lesson_info')

    def get_lesson_info(self, gradebook):
        lesson = gradebook.group.lesson
        return {'name': lesson.name, 'max_grade': lesson.max_grade, 'exam_grade': lesson.exam_grade}

    class Meta:
        model = GradeBook
        fields = ('id', 'group', 'columns', 'exam', 'lesson')
