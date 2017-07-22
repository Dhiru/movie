from django.shortcuts import render
from movieapp.models import Movie
from rest_framework import viewsets
from movieapp.serializers import MovieSerializer
from rest_framework import generics


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieList(generics.ListAPIView):
    model = Movie
    serializer_class = MovieSerializer

    def queryset(self):
        movie_name = self.kwargs['movie']
        return list(Movie.objects.filter(name__icontains=movie_name))
