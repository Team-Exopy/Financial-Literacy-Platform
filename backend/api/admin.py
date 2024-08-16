# Import necessary modules and models for the admin interface
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Subclass the UserAdmin class to customize the admin interface for the User model
class UserModelAdmin(BaseUserAdmin):
    
    # Override the default behavior to prevent users from creating new users
    # through the admin interface.
    def has_add_permission(self, request):
        return False

    # Override the default behavior to prevent users from deleting users
    # through the admin interface.
    def has_delete_permission(self, request, obj=None):
        return False

    # Make all fields read-only in the admin interface.
    def get_readonly_fields(self, request, obj=None):
        return self.get_fields(request, obj)

    # Define which fields to display in the admin interface
    list_display = ('id', 'username', 'is_admin', 'is_active', 'first_name', 'last_name', 'email', 'user_created')

    # Define which fields to filter by in the admin interface
    list_filter = ('is_admin',)

    # Define the fieldsets for the admin interface
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Important Dates', {'fields': ('user_created', 'last_login')}),
    )

    # Define the fields to display when adding a new user in the admin interface
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

    # Define which fields to search by in the admin interface
    search_fields = ('email', 'username', 'first_name', 'last_name')

    # Define the ordering of the admin interface
    ordering = ('id',)

    # Define which fields to display horizontally in the admin interface
    filter_horizontal = ()
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'duration')
    search_fields = ('title', 'course__title')
    list_filter = ('course',)
# Register the UserModelAdmin class with the User model for the admin interface
admin.site.register(User, UserModelAdmin)
admin.site.register(Conversation)
admin.site.register(Stock)
admin.site.register(Video,VideoAdmin)
admin.site.register(Course)
# Register other models with default admin interfaces
