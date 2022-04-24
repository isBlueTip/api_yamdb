from datetime import datetime

from django.db.models import Avg
from rest_framework import serializers

from titles.models import Category
from titles.models import Genre
from titles.models import Title


class CategorySerializer(serializers.ModelSerializer):
    """Serializer to work with categories."""
    class Meta:
        exclude = ["id"]
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    """Serializer to work with genres."""
    class Meta:
        exclude = ["id"]
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    """Serializer to work with titles."""
    genre = GenreSerializer(required=True, many=True)
    category = CategorySerializer(required=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = (
            "id",
            "name",
            "year",
            "rating",
            "description",
            "category",
            "genre",
        )

    def get_rating(self, obj):
        rating = obj.reviews.aggregate(Avg("score")).get("score__avg")
        if rating is None:
            return rating
        return int(rating)

    def validate(self, data):
        """Validate if title release year is not
        greater than current year."""
        release_year = data.get('year')
        today = datetime.now().year
        if today < release_year:
            raise serializers.ValidationError(
                "Нельзя добавлять произведения, которые еще не вышли"
            )
        return data


class TitlePostSerializer(serializers.ModelSerializer):
    """Serializer to work with posts under a specific title."""
    genre = serializers.SlugRelatedField(
        slug_field="slug", many=True, queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field="slug", many=False, queryset=Category.objects.all()
    )

    class Meta:
        model = Title
        fields = (
            "id",
            "name",
            "year",
            "description",
            "category",
            "genre",
        )
