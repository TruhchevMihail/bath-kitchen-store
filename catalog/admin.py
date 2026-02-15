from django.contrib import admin
from .models import Category, Product, Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'slug',)
    list_filter = ('section',)
    search_fields = ('title', 'slug',)
    prepopulated_fields = {'slug': ('title',),}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "brand", "category", "price", "sold_count", "created_at")
    list_filter = ("category__section", "brand", "category")
    search_fields = ("title", "slug", "brand__name", "category__title")
    prepopulated_fields = {"slug": ("title",)}
