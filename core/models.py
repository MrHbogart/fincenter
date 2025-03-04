from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    rank = models.CharField(max_length=20, choices=[('user', 'User'), ('admin', 'Admin')], default='user')
    phone_number = models.CharField(max_length=15, blank=True, null=True)

class FileHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_file = models.CharField(max_length=255)
    processed_file = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)




'''
    User Model
        Purpose: Custom user model extending Django's AbstractUser.

        Fields:
            rank: User role (e.g., user, admin).
            phone_number: Optional phone number for the user.

        Usage: Used for authentication and user management.

    File Model
        Purpose: Represents uploaded files by users.

        Fields:
            user: ForeignKey to the User model.
            file: FileField to store the uploaded file.
            uploaded_at: Timestamp of when the file was uploaded.

        Usage: Tracks files uploaded by users.

    FileHistory Model
        Purpose: Tracks the history of file uploads and processing.

        Fields:
            user: ForeignKey to the User model.
            original_file: Name of the original uploaded file.
            processed_file: Name of the processed file.
            uploaded_at: Timestamp of when the file was uploaded.

        Usage: Maintains a log of file processing activities.

'''