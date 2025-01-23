from django.db import models

class Task(models.Model):
    title=models.CharField('Задача', max_length=200)
    date=models.DateField('Дата окончания')
    completed=models.BooleanField('Завершено', default=False)

    def __str__(self):
        return self.title
