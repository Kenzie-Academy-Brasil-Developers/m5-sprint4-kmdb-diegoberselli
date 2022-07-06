from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    username = None
    email = serializers.EmailField()
    date_joined = serializers.DateTimeField(read_only=True)
    password = serializers.CharField(write_only=True)
    update_at = serializers.DateTimeField(read_only=True)

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("email already exists")
        return value

    def create(self, validated_data):

        validated = User.objects.create_user(**validated_data)

        return validated


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
