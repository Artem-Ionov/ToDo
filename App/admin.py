from django.contrib import admin
from .models import Task, TaskBlock

admin.site.register(Task)

class TaskInline(admin.TabularInline):
    model=Task
    extra=0

class TaskBlockAdmin(admin.ModelAdmin):
    inlines=[TaskInline]
    list_display=['title', 'user']

admin.site.register(TaskBlock, TaskBlockAdmin)
