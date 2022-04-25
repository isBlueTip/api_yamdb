from rest_framework import serializers

from titles.models import Category, Genre, Title


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
    rating = serializers.IntegerField()

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


class TitlePostSerializer(serializers.ModelSerializer):
    """Serializer to create new titles."""
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
