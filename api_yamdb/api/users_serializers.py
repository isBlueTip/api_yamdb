from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
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


class TokenSerializer(serializers.ModelSerializer):
    username = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = User
        fields = ['username', 'confirmation_code']

    def validate(self, data):
        username = self.initial_data.get('username')
        if username is None:
            raise serializers.ValidationError(
                'Введите username.')
        user = get_object_or_404(User, username=username)
        true_otp = user.confirmation_code
        passed_otp = self.initial_data.get('confirmation_code')
        if passed_otp != true_otp:
            raise serializers.ValidationError(
                'Введите действующий код подтверждения.')
        return data


# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ['pk', 'username', 'first_name',
#                   'last_name', 'email', 'bio', 'role']  # TODO delete pk