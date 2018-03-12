from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'content']
    ordering = ['title']
    date_hierarchy = 'updated'


admin.site.register(Post, PostAdmin)
