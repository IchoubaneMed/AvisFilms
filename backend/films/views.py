from django.shortcuts import render
from django.db.models import Avg
from rest_framework import generics, viewsets
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework.response import Response

# Create your views here.

class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    def get_queryset(self):
        return Movie.objects.all().annotate(average=Avg("review__grade")).order_by('-id')

class MovieDetailView(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all().annotate(average=Avg("review__grade"))
    serializer_class = MovieSerializer

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        movie_id = self.request.data['movie'] 
        movie = Movie.objects.get(id=movie_id)
        serializer.save(movie=movie)

    
