from rest_framework import serializers

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']

    def validate_username(self, username):
        if username == 'me':
            raise serializers.ValidationError(
                'Используйте другое имя пользователя.')
        return username


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    def validate(self, data):
        username = data.get('username')
        user = get_object_or_404(User, username=username)
        true_otp = user.confirmation_code
        passed_otp = data.get('confirmation_code')
        if passed_otp != true_otp:
            raise serializers.ValidationError(
                'Введите действующий код подтверждения.')
        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'role',
                  'first_name', 'last_name', 'bio']
