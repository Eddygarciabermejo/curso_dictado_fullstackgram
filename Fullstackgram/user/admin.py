from django.contrib import admin
from user.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone_number', 'website', 'profile_picture')
    list_display_links = ('pk', 'user')
    list_editable = ('website', 'profile_picture')

    search_field = (
        'user'
    )
    fieldsets = (

    )
    readonly_fields = (
        
    )