from rest_framework import serializers

from .models import User, Profile, Group


class ShortUserInfoSerializer(serializers.ModelSerializer):
    """"Короткі данні про користувача(ім'я і ід)"""

    class Meta:
        model = User

        fields = ['first_name', 'last_name', 'id']


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

    user_profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'user_profile']
