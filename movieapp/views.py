from django.shortcuts import render
from movieapp.models import Movie
from rest_framework import viewsets
from movieapp.serializers import MovieSerializer
from rest_framework import generics
from rest_framework.response import Response


class MovieViewSet(viewsets.ViewSet):
    """
        Listing list of movies
        urls: <domain>/movies
            - it will list all movies
        urls: <domain>/movies?name=avenger
            - it will filter the movie with name
        urls: <domain>/movies?imdb_score=8  
            - it will filter the movie with imdb            
    """
    def list(self, request):
        dict_value = request.GET.dict()
        if dict_value == {}:
            queryset = Movie.objects.all()
        else:
            key = dict_value.keys()[0]
            value = dict_value[key]
            kwargs = {'{0}__icontains'.format(key): value}
            queryset = Movie.objects.filter(**kwargs)    
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

