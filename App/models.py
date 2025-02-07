from django.db import models

class Task_block(models.Model):
    title=models.CharField('Блок задач', max_length=200)
    
    class Meta:
        ordering=['title']

    def __str__(self):
        return self.title
    

class Task(models.Model):
    title=models.CharField('Задача', max_length=200)
    date=models.DateField('Дата окончания', blank=True, null=True)
    completed=models.BooleanField('Завершено', default=False)
    block=models.ForeignKey(Task_block, on_delete=models.SET_NULL, null=True, verbose_name='Тема')

    importance_dict={'в': 'Высокая', 'н': 'Норм'}
    importance=models.CharField('Важность', max_length=1, choices=importance_dict, default='н')

    class Meta:
        ordering=['block', 'importance', 'title']
        
    def __str__(self):
        return self.title
    
    

