from django.db import models

class Task(models.Model):
    "Модель задачи"
    title = models.CharField('Название', max_length=200)               
    date = models.DateField('Дата окончания', blank=True, null=True)    
    description = models.TextField('Описание', blank=True, null=True)
    completed = models.BooleanField('Завершено', default=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
