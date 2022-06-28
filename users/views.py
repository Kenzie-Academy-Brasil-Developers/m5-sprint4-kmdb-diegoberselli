from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User

from users.serializers import RegisterSerializer


class RegisterView(APIView):
    def get(self, request):
        
        return Response({"message": "ok"})

    def post(self, request):
        
        serializer = RegisterSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
  
        serializer.save()
   
        return Response(serializer.data, status=status.HTTP_201_CREATED)