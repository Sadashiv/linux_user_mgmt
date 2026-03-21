from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
    username = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    def __unicode__(self):
        return self.user.username

class User(models.Model):
    username   = models.CharField(max_length=150, unique=True)
    email      = models.EmailField(max_length=255, unique=True)
    password   = models.CharField(max_length=255)
    website    = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'    # maps to the exact table name in psql

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    website = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'usermgmt_userprofile'

    def __str__(self):
        return self.user.username
