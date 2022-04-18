from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, PrimaryKeyRelatedField

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

    def create(self, validated_data):
        author = validated_data.get('author')
        title = get_object_or_404(Title, pk=validated_data.get('title_id'))
        if title.reviews.filter(author=author).exists():
            raise serializers.ValidationError(detail='Вы уже оставили отзыв на'
                                              ' это произведение.')
        review = Review.objects.create(**validated_data)
        return review


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    review = PrimaryKeyRelatedField(write_only=True,
                                    queryset=Review.objects.all(),
                                    required=False)

    class Meta:
        fields = ['id', 'review', 'text', 'author', 'pub_date']
        model = Comment
