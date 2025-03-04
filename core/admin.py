from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, FileHistory

# Register the custom user model
admin.site.register(User, UserAdmin)


@admin.register(FileHistory)
class FileHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'original_file', 'processed_file', 'uploaded_at')
    list_filter = ('user', 'uploaded_at')
    search_fields = ('user__username', 'original_file', 'processed_file')


'''
    UserAdmin
        Purpose: Customizes the display of the User model in the Django admin panel.

        Fields Displayed:
            username, email, phone_number, rank, is_staff.

        Usage: Enhances the admin interface for user management.

    FileAdmin
        Purpose: Customizes the display of the File model in the Django admin panel.

        Fields Displayed:
            user, file, uploaded_at.

        Usage: Enhances the admin interface for file management.

    FileHistoryAdmin
        Purpose: Customizes the display of the FileHistory model in the Django admin panel.

        Fields Displayed:
            user, original_file, processed_file, uploaded_at.

        Usage: Enhances the admin interface for file history management.

'''