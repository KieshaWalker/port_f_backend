from django.contrib import admin
from .models import Profile, Project

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    readonly_fields = ['id']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'technologies']
    readonly_fields = ['id', 'created_at']
