from django.shortcuts import render

from rest_framework import generics
from .models import Recipe, Review
from .serializers import RecipeSerializer, ReviewSerializer

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer