from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)

    class Meta:
        db_table = "movie"

