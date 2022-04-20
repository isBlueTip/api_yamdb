from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField, SlugRelatedField

from reviews.models import Comment, Review
from titles.models import Title


class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    title = PrimaryKeyRelatedField(write_only=True,
                                   queryset=Title.objects.all(),
                                   required=False)

    class Meta:
        fields = ['id', 'title', 'text', 'author', 'score', 'pub_date']
        model = Review

    def validate(self, data):
        """Проверка уникальности отзыва от пользователя на произведение."""
        title = get_object_or_404(
            Title, id=self.context['view'].kwargs.get("title_id")
        )
        author = self.context.get('request').user
        if (title.reviews.filter(author=author).exists()
                and self.context['request'].method == 'POST'):
            raise serializers.ValidationError(detail='Вы уже оставили отзыв на'
                                              ' это произведение.')
        return data

    def validate_score(self, value):
        """Проверка: score в диапазоне от 1 до 10"""
        if not (1 <= value <= 10):
            raise serializers.ValidationError('Оценка должна быть от 1 до 10.')
        return value


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    review = PrimaryKeyRelatedField(write_only=True,
                                    queryset=Review.objects.all(),
                                    required=False)

    class Meta:
        fields = ['id', 'review', 'text', 'author', 'pub_date']
        model = Comment
