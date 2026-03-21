from django.contrib import admin
from usermgmt.models import UserDetails
from usermgmt.models import User

# Register your models here.
admin.site.register(UserDetails)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display  = ['id', 'username', 'email', 'website', 'created_at']
    search_fields = ['username', 'email']
    list_filter   = ['created_at']
    ordering      = ['-created_at']
