from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    "Модель задачи"
    title = models.CharField('Название', max_length=200)                # Поля модели
        # Связь с моделью блока задач (внешний ключ)
    taskblock = models.ForeignKey('TaskBlock', on_delete=models.SET_NULL, null=True, verbose_name='Блок задач')
    importance = models.BooleanField('Важность', default=False)               
    date = models.DateField('Дата окончания', blank=True, null=True)    
    completed = models.BooleanField('Завершено', default=False)
    description = models.TextField('Описание', blank=True, null=True)

    class Meta:
        ordering = ['title']            # Сортировка по названию задачи
        verbose_name = "Задача"         # Задаём название модели на русском (для админ-панели)
        verbose_name_plural = "Задачи"  # То же самое для множественного числа

    def __str__(self):
        return self.title               # При обращении к экземпляру модели возвращаем название задачи (для админ-панели)
    

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
