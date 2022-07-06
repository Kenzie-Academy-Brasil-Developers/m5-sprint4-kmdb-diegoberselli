import ipdb
from movies.models import Movie
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from reviews.models import Review
from reviews.permissions import IsAdminOrIsOwnUser
from reviews.serializers import ReviewSerializer


class ReviewView(APIView, PageNumberPagination):
    def get(self, request):
        reviews = Review.objects.all()
        reviews = self.paginate_queryset(reviews, request, view=self)
        serializer = ReviewSerializer(reviews, many=True)
        return self.get_paginated_response(serializer.data)


class ReviewDetailsView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, movie_id):

        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
            )
        reviews = movie.reviews.all()
        result_page = self.paginate_queryset(reviews, request, view=self)
        serializer = ReviewSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, movie_id):

        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie, critic=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeteleReviewView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrIsOwnUser]

    def delete(self, request, review_id):
        try:
            review = Review.objects.get(id=review_id)
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Review.DoesNotExist:
            return Response(
                {"message": "Review not found"}, status=status.HTTP_404_NOT_FOUND
            )
