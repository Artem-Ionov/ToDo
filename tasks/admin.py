from django.contrib import admin
from .models import Task, TaskBlock

class TaskAdmin(admin.ModelAdmin):  
    "Кастомизация админ-панели"      
    # Выбираем поля и их порядок в списке задач          
    list_display = ('title', 'taskblock', 'display_user', 'importance', 'deadline', 'completed', 'archive') 
    # Добавляем фильтры
    list_filter = ('importance', 'deadline', 'completed', 'archive')           
    # Выбираем поля и их порядок в подробном описании задачи
    fields = ['title', 'taskblock', 'importance', 'deadline', 'completed', 'description', ('archive', 'archive_date')]  

class TaskInline(admin.TabularInline):
    "Отображение задач для каждого блока (горизонтальная компановка)"
    model = Task
    extra = 0                               # Устраняем пустые поля в конце

class TaskBlockAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    list_filter = ['user']
    inlines = [TaskInline]

admin.site.register(Task, TaskAdmin)        # Регистрация моделей в админ-панели
admin.site.register(TaskBlock, TaskBlockAdmin)
