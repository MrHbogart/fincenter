from django.urls import path
from .views import ProcessExcelView, FileHistoryView
from .views import UserRegistrationView, UserLoginView, UserLogoutView

urlpatterns = [
    path('process-excel/', ProcessExcelView.as_view(), name='process-excel'),
    path('file-history/', FileHistoryView.as_view(), name='file-history'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    
]



'''
    URL Patterns
        Purpose: Defines API endpoints for the application.

        Endpoints:
            /register/: User registration.
            /login/: User login.
            /upload/: File upload.
            /file-history/: File history retrieval.
            /process-excel/: Excel file processing.

        Usage: Maps URLs to views for API routing.

'''