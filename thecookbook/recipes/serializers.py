from rest_framework import serializers
from .models import Recipe, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'recipe', 'username', 'rating', 'comment', 'created_at', 'updated_at']

class RecipeSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 'title','cusine', 'description', 'image_url', 'prep_time', 
            'cook_time', 'difficulty', 'servings', 'ingredients', 
            'instructions', 'created_at', 'updated_at', 'average_rating', 'reviews', 
        ]