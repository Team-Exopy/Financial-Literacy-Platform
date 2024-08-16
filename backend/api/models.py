from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import timedelta

# Custom user manager
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, username, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, username, password=None):
        user = self.create_user(email, first_name, last_name, username, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom user model
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    user_created = models.DateTimeField(default=timezone.now)
    premium = models.BooleanField(default=False)
    webapp_currency = models.PositiveIntegerField(default=0)  # Webapp currency field
    points = models.PositiveIntegerField(default=0)  # Points field

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def make_premium(self):
        if self.premium:
            raise ValidationError('User is already a premium member.')
        self.premium = True
        self.webapp_currency += 100000  # Add 100,000 webapp currency
        self.save()

    def redeem_currency_for_points(self):
        if self.webapp_currency >= 100000:
            self.points += 100  # Convert 100,000 currency to 100 points
            self.webapp_currency -= 100000
            self.save()
        else:
            raise ValidationError('Not enough webapp currency to redeem points.')

    def redeem_points_for_course(self, course):
        if course.is_premium and self.points >= course.points_required:
            self.points -= course.points_required
            self.save()
            # Logic to grant course access can be added here
            return course.videos.all()  # Return all videos associated with the course
        else:
            raise ValidationError('Not enough points to redeem this course.')

# Course model
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_premium = models.BooleanField(default=False)
    points_required = models.PositiveIntegerField(default=0)  # Points required to redeem this course

    def __str__(self):
        return self.title

# Video model
class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/',blank=True, null=True)  # Upload video file from the device
    duration = models.DurationField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

# Conversation model
class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        now = timezone.now()
        last_24_hours = now - timedelta(hours=24)
        recent_messages_count = self.user.conversations.filter(timestamp__gte=last_24_hours).count()
        
        if not self.user.premium and recent_messages_count >= 4:
            raise ValidationError('Non-premium users can only send 4 messages every 24 hours.')
        
        super().save(*args, **kwargs)

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    trend = models.CharField(max_length=10, choices=[
        ('UP', 'Up'),
        ('DOWN', 'Down'),
        ('FLAT', 'Flat')
    ])