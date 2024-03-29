from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    #The additional attributes we wish to include
    website = models.URLField(blank=True)

    #Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class UserDetails(models.Model):
    username = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    def __unicode__(self):
        return self.user.username


