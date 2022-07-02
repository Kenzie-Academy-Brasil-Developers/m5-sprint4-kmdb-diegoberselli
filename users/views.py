import ipdb
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.permissions import UserIsAdmin
from users.serializers import LoginSerializer, RegisterSerializer


class RegisterView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserIsAdmin]

    def get(self, request):

        user = User.objects.all()
        serializer = RegisterSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RegisterDetailView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserIsAdmin]
    
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = RegisterSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key})

        return Response(
            {"detail": "invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED
        )
