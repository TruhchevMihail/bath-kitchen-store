from django.contrib import admin
from .models import ProjectPost


@admin.register(ProjectPost)
class ProjectPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'created_at',)
    list_filter = ('section', 'created_at',)
    search_fields = ('title', 'slug', 'excerpt',)
    prepopulated_fields = {'slug': ('title',),}
    filter_horizontal = ('related_products',)