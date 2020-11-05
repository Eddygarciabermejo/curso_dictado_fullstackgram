from django.contrib import admin
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'profile', 'title', 'photo')
    list_display_links = ('pk', 'user')
    list_editable = ('title', 'photo')

    search_field = (
        'user',
        'title'
    )
    fieldsets = (

    )
    readonly_fields = (
        
    )
# Register your models here.
