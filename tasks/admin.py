from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):  
    "Класс для кастомизации админ-панели"                
    list_display = ('title', 'importance', 'date', 'completed')           # Выбираем поля и их порядок в списке задач
    list_filter = ('date', 'importance', 'completed')                     # Добавляем фильтры
    fields = ['title', 'importance', 'date', 'completed', 'description']  # Выбираем поля и их порядок в подробном описании задачи

admin.site.register(Task, TaskAdmin)
