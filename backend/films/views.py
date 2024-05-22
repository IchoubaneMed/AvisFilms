from django.db.models import Avg
from rest_framework import generics
from .models import Movie, Review, Actor
from .serializers import MovieSerializer, ReviewSerializer, ActorSerializer
from .tasks import simulate_processing
# Create your views here.

class ActorListView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    def get_queryset(self):
        return Movie.objects.all().annotate(average=Avg("review__grade")).order_by('id')

class MovieDetailView(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all().annotate(average=Avg("review__grade"))
    serializer_class = MovieSerializer

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        movie_id = self.request.data['movie'] 
        movie = Movie.objects.get(id=movie_id)
        # Appeler la tâche Celery pour simuler le traitement pendant 10 secondes
        simulate_processing.delay(movie_id)
        serializer.save(movie=movie)
        
    
