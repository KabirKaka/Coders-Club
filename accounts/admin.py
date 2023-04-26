from django.contrib import admin
from .models import UserProfile, Domain, ClubApplication, ClubMembership

class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Domain)

class ClubApplicationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Applicant Information', {
            'fields': ('user', 'position', 'portfolio_link', 'applied_date', 'domains'),
        }),
        ('Application Status', {
            'fields': ('accepted',),
        }),
    )
    readonly_fields = ('user', 'position', 'portfolio_link', 'applied_date', 'domains')

admin.site.register(ClubApplication, ClubApplicationAdmin)
# admin.site.register(ClubApplication)

admin.site.register(ClubMembership)