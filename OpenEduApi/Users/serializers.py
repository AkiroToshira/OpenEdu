from rest_framework import serializers

from .models import User, Profile, Group


class ShortUserInfoSerializer(serializers.ModelSerializer):
    """"Короткі данні про користувача(ПІБ і ід)"""
    middle_name = serializers.SerializerMethodField('middle_name_foo')

    """"Витягуємо по батькові з profile"""
    def middle_name_foo(self, user):
        return user.profile.middle_name

    class Meta:
        model = User

        fields = ('id', 'first_name', 'last_name', 'middle_name')


class GroupSerializer(serializers.ModelSerializer):
    """"Вивід данних про групу користувача"""

    curator = ShortUserInfoSerializer(read_only=True)

    class Meta:
        model = Group

        fields = ['name', 'departament', 'year', 'curator']


class ProfileSerializer(serializers.ModelSerializer):
    """"Вивід додаткових данних про користувача"""

    group = GroupSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['middle_name', 'group', 'numberphone', 'credit_book_number', 'img']


class UserSerializer(serializers.ModelSerializer):
    """"Вивід данних про користувача"""

    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'profile']
