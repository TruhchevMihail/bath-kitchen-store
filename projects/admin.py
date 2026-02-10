from django.contrib import admin
from .models import ProjestPost


@admin.register(ProjestPost)
class ProjestPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at',)
    search_fields = ('title', 'slug', 'excerpt',)
    prepopulated_fields = {'slug': ('title',),}
    filter_horizontal = ('related_products',)
