from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)