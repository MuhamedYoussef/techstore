from django.contrib import admin
from .models import Product, Category, Brand


@admin.register(Product)
class ProfuctAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price', 'best')


admin.site.register(Category)
admin.site.register(Brand)
