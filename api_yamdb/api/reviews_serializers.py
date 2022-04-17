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


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    review = PrimaryKeyRelatedField(write_only=True,
                                    queryset=Review.objects.all(),
                                    required=False)

    class Meta:
        fields = ['id', 'review', 'text', 'author', 'pub_date']
        model = Comment
