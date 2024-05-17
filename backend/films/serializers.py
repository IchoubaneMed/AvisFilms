from rest_framework import serializers
from .models import Actor, Review, Movie


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    average = serializers.DecimalField(max_digits=5, decimal_places=2, required=False, allow_null=True, read_only=True)
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "actors", "average")