from django.contrib import admin
from .models import UserProfile, Posts

@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    pass

@admin.register(Posts)
class AdminPosts(admin.ModelAdmin):
    pass