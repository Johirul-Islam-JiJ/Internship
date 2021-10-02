from django.contrib import admin
from .models import Blog, BlogCategory

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
    search_fields = ['category']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'author', 'created_at']
    search_fields = ['author', 'title']
    filter_fields = ['created_at']


admin.site.register(BlogCategory, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)