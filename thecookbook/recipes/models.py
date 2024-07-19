from django.db import models
from django.utils import timezone
from django.db.models import Avg
from django.core.validators import MaxValueValidator

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=False)
    CUISINE_CHOICES = [
        ('Indian', 'Indian'),
        ('Thai', 'Thai'),
        ('Chinese', 'Chinese'),
        ('Other', 'Other'),
    ]
    cusine = models.CharField(max_length = 20, choices=CUISINE_CHOICES, default='Other')
    description = models.TextField(blank=False)
    image_url = models.URLField(max_length=200, blank=False)
    prep_time = models.PositiveIntegerField(blank=False)  # ime is in minutes
    cook_time = models.PositiveIntegerField(blank=False)  # time is in minutes
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_CHOICES)
    servings = models.PositiveIntegerField(blank=False)
    ingredients = models.JSONField(blank=False)  # Requires PostgreSQL or Django 3.1+
    instructions = models.JSONField(blank=False)  # Requires PostgreSQL or Django 3.1+
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    average_rating = models.FloatField(default=0.0)
    rating_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def update_rating(self):
        reviews = self.reviews.all()
        self.rating_count = reviews.count()
        self.average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
        self.save()


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    username = models.CharField(max_length=255, blank=False)
    rating = models.PositiveIntegerField(blank=False, validators=[MaxValueValidator(5)])  # Assuming rating is from 1-5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.username} for {self.recipe.title}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.recipe.update_rating()