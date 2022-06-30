from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users import serializers

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieView(APIView):
    def get(self, request):

        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieViewDetail(APIView):
    
    def get(self, request, movie_id):
        
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"message": "Movie not found"}, status=status.HTTP_200_OK
            )
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)