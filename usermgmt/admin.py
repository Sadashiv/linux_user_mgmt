from django.contrib import admin
from usermgmt.models import UserProfile,UserDetails

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserDetails)
