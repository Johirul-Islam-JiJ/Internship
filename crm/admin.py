from django.contrib import admin
from .models import Customer, Product, Tag, Order

# Register your models here.

class OrderInline(admin.TabularInline):
    model = Order

class TagInline(admin.TabularInline):
    model = Order.tags.through

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'product_id', 'created_at']
    search_fields = ['name']
    inlines = [TagInline, ]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    search_fields = ['phone', 'email', 'name']
    filter_fields = ['created_at']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name', 'category']
    filter_fields = ['created_at']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Order, OrderAdmin)

