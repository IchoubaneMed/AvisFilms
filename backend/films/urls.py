from django.urls import path
from .views import MovieListView, MovieDetailView, ReviewCreateView


urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movies/<int:id>/review/', ReviewCreateView.as_view(), name='review_create'),
]

