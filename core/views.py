import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import FileUploadSerializer, UserRegistrationSerializer, UserLoginSerializer
from .models import User, FileHistory
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate



class ProcessExcelView(APIView):

    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            df = pd.read_excel(file)

            # Example: Process the file (e.g., add a new column)
            df['Processed'] = df['Amount'] * 1.1  # Example calculation

            # Save processed file
            output_file = 'processed_file.xlsx'
            df.to_excel(output_file, index=False)

            # Save file history
            FileHistory.objects.create(user=request.user, original_file=file.name, processed_file=output_file)

            return Response({'message': 'File processed successfully', 'file': output_file}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class FileHistoryView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        history = FileHistory.objects.filter(user=request.user)
        data = [{'original_file': h.original_file, 'processed_file': h.processed_file, 'uploaded_at': h.uploaded_at} for h in history]
        return Response(data, status=status.HTTP_200_OK)
    


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)  # Create a token for the user
            return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)  # Get or create a token for the user
                return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()  # Delete the token
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
    


'''
    UserRegistrationView
        Purpose: Handles user registration.

        Methods:
            post: Validates and creates a new user, returns a token.

        Usage: Public endpoint for user sign-up.

    UserLoginView
        Purpose: Handles user login.

        Methods:
            post: Validates credentials, returns a token.

        Usage: Public endpoint for user login.

    FileUploadView
        Purpose: Handles file uploads.

        Methods:
            post: Validates and saves uploaded files, creates FileHistory records.

        Usage: Authenticated endpoint for file uploads.

    FileHistoryView
        Purpose: Retrieves file history for authenticated users.

        Methods:
            get: Returns a list of file history records for the user.

        Usage: Authenticated endpoint for accessing file history.

    ProcessExcelView
        Purpose: Processes uploaded Excel files.

        Methods:
            post: Reads the uploaded file, processes it, and returns the processed file.

        Usage: Authenticated endpoint for file processing.

'''