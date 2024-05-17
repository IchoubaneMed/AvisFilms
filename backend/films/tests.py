from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Movie
# Create your tests here.

class MovieAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(title='Existing Movie', description='Existing Description')

    def test_get_movie_list(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_movie_detail(self):
        response = self.client.get(reverse('movie_detail', kwargs={'pk': self.movie.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ReviewAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(title='Test Movie', description='Test Description')
        self.review_data = {'grade': 5, 'movie': self.movie.pk}

    def test_create_review(self):
        response = self.client.post(reverse('review_create', kwargs={'id': self.movie.pk}), self.review_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    