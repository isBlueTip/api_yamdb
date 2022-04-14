from rest_framework import serializers
from titles.models import Categories


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Categories
