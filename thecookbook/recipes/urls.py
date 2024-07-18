from django.urls import path
from .views import RecipeListCreateView, ReviewListCreateAPIView

urlpatterns = [
    path('items/', RecipeListCreateView.as_view(), name='item-list-create'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-create'), 
]
