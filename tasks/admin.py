from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at', 'updated_at')
    list_filter = ('completed', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    list_editable = ('completed',)
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Task, TaskAdmin)