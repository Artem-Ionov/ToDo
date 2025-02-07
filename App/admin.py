from django.contrib import admin
from .models import Task, Task_block

admin.site.register(Task)

class TaskInline(admin.TabularInline):
    model=Task
    extra=0

class Task_blockAdmin(admin.ModelAdmin):
    inlines=[TaskInline]

admin.site.register(Task_block, Task_blockAdmin)
