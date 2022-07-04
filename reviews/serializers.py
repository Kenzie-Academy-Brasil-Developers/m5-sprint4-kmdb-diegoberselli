from rest_framework import serializers
from users.models import User

from .models import Review


class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']
        

class ReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'stars', 'review', 'spoilers', 'recommendation','critic' , 'movie_id']
        read_only_fields = ['id', 'movie_id', 'critic']
        extra_kwargs = {'stars': {'max_value':10, 'min_value':1}}


    def create(self, validated_data):
        review = Review.objects.create(**validated_data)

        return review
