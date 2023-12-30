from django.contrib import admin
from .models import UserProfile, Posts, UsersFirendsList

@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    pass

@admin.register(Posts)
class AdminPosts(admin.ModelAdmin):
    pass

@admin.register(UsersFirendsList)
class AdminUsersFirendsList(admin.ModelAdmin):
    pass