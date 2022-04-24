from rest_framework import serializers

from django.shortcuts import get_object_or_404

from users.models import User


class SignupSerializer(serializers.ModelSerializer):
    """Serializer to register new users."""

    class Meta:
        model = User
        fields = ['username', 'email']

    def validate_username(self, username):
        # username 'me' is restricted
        if username == 'me':
            raise serializers.ValidationError(
                'Используйте другое имя пользователя.')
        return username


class TokenSerializer(serializers.Serializer):
    """Serializer to work with sending JWT token."""
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    def validate(self, data):
        """Validate OTP."""
        username = data.get('username')
        user = get_object_or_404(User, username=username)
        true_otp = user.confirmation_code
        passed_otp = data.get('confirmation_code')
        # compare otp from json against the one from db
        if passed_otp != true_otp:
            raise serializers.ValidationError(
                'Введите действующий код подтверждения.')
        return data


class UserSerializer(serializers.ModelSerializer):
    """Serializer to work with User model."""

    class Meta:
        model = User
        fields = ['username', 'email', 'role',
                  'first_name', 'last_name', 'bio']
