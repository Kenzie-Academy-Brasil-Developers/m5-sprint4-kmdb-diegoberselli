from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    premiere = serializers.DateField()
    duration = serializers.CharField(max_length=10)
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()

    genre = GenreSerializer(many=True)

    def create(self, validated_data):

        genre_data = validated_data.pop("genre")
        movie = Movie.objects.create(**validated_data)

        for gen in genre_data:
            genre_choice, _ = Genre.objects.get_or_create(**gen)
            movie.genre.add(genre_choice)

        return movie

    def update(self, instance: Movie, validated_data: dict):

        genre_data = validated_data.pop("genre", None)
        if genre_data:
            instance.genre.clear()
            for gen in genre_data:
                verify, _ = Genre.objects.get_or_create(**gen)
                instance.genre.add(verify)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
