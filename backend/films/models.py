from django.db import models

# Create your models here.

class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return "{} - {}".format(self.first_name, self.last_name)
    
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    actors = models.ManyToManyField(Actor)
    def __str__(self):
        return self.title
    
class Review(models.Model):
    grad = models.FloatField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review")
