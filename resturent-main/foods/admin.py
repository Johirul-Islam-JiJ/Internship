from django.contrib import admin
from .models import FoodCategory, Food


# Register your models here.

class FCAdmin(admin.ModelAdmin):
    list_display = ('food_category_name', 'isActive')


class FAdmin(admin.ModelAdmin):
    list_display = ('category', 'food_name', 'title', 'slug', 'isActive')
    list_filter = ('category', 'food_name', 'slug', 'isActive')
    search_fields = ['category', 'food_name', 'slug']

    prepopulated_fields = {'slug': ('food_name')}


admin.site.register(FoodCategory)
admin.site.register(Food)