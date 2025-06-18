from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    "Модель задачи"
    title = models.CharField('Задача', max_length=200)                # Поля модели
        # Связь с моделью блока задач (внешний ключ)
    taskblock = models.ForeignKey('TaskBlock', on_delete=models.SET_NULL, null=True, verbose_name='Блок задач')
    importance = models.BooleanField('Важность', default=False)               
    deadline = models.DateField('Срок', blank=True, null=True)    
    completed = models.BooleanField('Сделано', default=False)
    description = models.TextField('Описание', blank=True, null=True)
    archive = models.BooleanField('В архиве', default=False)
    archive_date = models.DateField('Дата помещения в архив', blank=True, null=True)

    class Meta:
        ordering = ['title']            # Сортировка по названию задачи
        verbose_name = "Задача"         # Задаём название модели на русском (для админ-панели)
        verbose_name_plural = "Задачи"  # То же самое для множественного числа

    def __str__(self):
        return self.title               # При обращении к экземпляру модели возвращаем название задачи (для админ-панели)
    
    def display_user(self):
        "Отображение имени пользователя в админ-панели для задач (имя пользователя определено в модели блока)"
        return self.taskblock.user
    display_user.short_description = 'Пользователь'
    
    
class TaskBlock(models.Model):
    "Модель блока задач"
    title = models.CharField('Блок задач', max_length = 100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')

    class Meta:
        ordering = ['title']
        verbose_name = 'Блок задач'
        verbose_name_plural = 'Блоки задач'

    def __str__(self):
        return self.title
