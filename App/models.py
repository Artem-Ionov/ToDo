from django.db import models

class Task(models.Model):
    title=models.CharField('Задача', max_length=200)
    date=models.DateField('Дата окончания')
    completed=models.BooleanField('Завершено', default=False)

    class Meta:
        ordering=['date']
        
    def __str__(self):
        return self.title
    

class Question_block(models.Model):
    title=models.CharField('Группа вопросов', max_length=200) 

    class Meta:
        ordering=['title']

    def __str__(self):
        return self.title


class Question(models.Model):
    title=models.CharField('Вопрос', max_length=200, default='?')
    decision=models.TextField('Решение', blank=True, default='Пока не найдено')
    block=models.ForeignKey(Question_block, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering=['title']

    def __str__(self):
        return self.title
    

