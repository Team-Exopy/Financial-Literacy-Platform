# Import the necessary modules for user management
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator


# Define a custom user manager class
class UserManager(BaseUserManager):
    # Create a new user
    def create_user(self, email, first_name, last_name, username, password=None):
        # Check if the email is provided
        if not email:
            raise ValueError('User must have an email address')
        # Check if the username is provided
        if not username:
            raise ValueError('User must have a username')

        # Create a new user instance
        user = self.model(
            email=self.normalize_email(email),  # Normalize the email address
            first_name=first_name,  # Set the first name
            last_name=last_name,  # Set the last name
            username=username,  # Set the username
            password = password,
            is_admin=False,  # Set the user as not an admin
        )
        # Set the password for the user
        user.set_password(password)
        # Save the user to the database
        user.save(using=self._db)
        # Return the created user
        return user

    # Create a new superuser
    def create_superuser(self, email, first_name, last_name, username, password=None):
        # Create a new user
        user = self.create_user(email, first_name, last_name, username, password)
        # Set the user as an admin
        user.is_admin = True
        # Save the user to the database
        user.save(using=self._db)
        # Return the created superuser
        return user

# Define the custom user model
class User(AbstractBaseUser):
    # Define the fields for the user model
    first_name = models.CharField(max_length=50)  # First name of the user
    last_name = models.CharField(max_length=50)  # Last name of the user
    username = models.CharField(max_length=50, unique=True)  # Username of the user
    email = models.EmailField(max_length=200, unique=True)  # Email address of the user
    password = models.CharField(max_length=255)  # Password for the user
    is_admin = models.BooleanField(default=False)  # Whether the user is an admin or not
    user_created = models.DateTimeField(default=timezone.now)  # Date and time when the user was created

    # Set the custom user manager for this model
    objects = UserManager()

    # Set the username field to be the email field
    USERNAME_FIELD = 'email'
    # Set the required fields for creating a user
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # Override the __str__ method to return the email of the user
    def __str__(self):
        return self.email

    # Override the has_perm method to check if the user is an admin
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return self.is_admin

    # Override the has_module_perms method to always return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'?"
        return True

    # Override the is_staff property to check if the user is an admin
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

    # Validate the username to ensure it is not blank
    def validate_username(self, value):
        if not value:
            raise ValidationError('Username cannot be blank')


class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    trend = models.CharField(max_length=10, choices=[
        ('UP', 'Up'),
        ('DOWN', 'Down'),
        ('FLAT', 'Flat')
    ])