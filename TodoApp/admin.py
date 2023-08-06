from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class UserAdmin(admin.ModelAdmin):
    list_display = ('task','is_completed','created_at','updated_at')
    search_fields= ('task',)