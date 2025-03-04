from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensure password is write-only

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number', 'rank']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number', ''),
            rank=validated_data.get('rank', 'user'),
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)



'''
    UserRegistrationSerializer
        Purpose: Handles user registration data.

        Fields:
            username, email, password, phone_number, rank.

        Usage: Validates and creates new user instances.

    UserLoginSerializer
        Purpose: Handles user login data.

        Fields:
            username, password.

        Usage: Validates login credentials.

    FileUploadSerializer
        Purpose: Handles file upload data.

        Fields:
            file: FileField for the uploaded file.

        Usage: Validates and processes file uploads.

    FileSerializer
        Purpose: Serializes File model instances.

        Fields:
            id, user, file, uploaded_at.

        Usage: Used in API responses for file-related endpoints.

'''