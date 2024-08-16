# This file contains the URL mappings for the user views.
# The URLs defined here are used to map the user views to the corresponding URLs.

# Import the necessary modules
from django.urls import path, include  # Import the path and include functions from the django.urls module

# Import the user views
from api.views.bot import *  # Import the user views from the api.views.user_views module

urlpatterns = [
    path('bot/', ChatbotView.as_view(), name='bot'),  
]
