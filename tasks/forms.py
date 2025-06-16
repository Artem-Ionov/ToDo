from django import forms
from .models import Task, TaskBlock

class TaskForm(forms.ModelForm):            # Используем для формы поля из модели
    "Форма для создания задачи и обновления параметров задачи"
    class Meta:
        model = Task
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        "Редактируем конструктор, чтобы в форме для задачи выводились только блоки задач текущего пользователя"
        # Извлекаем пользователя из списка входных именованных аргументов (с удалением - чтобы не передавать в суперкласс)
        self.user = kwargs.pop('user')  
        # Вызываем конструктор суперкласса - именно в нём происходит формирование полей формы    
        super(TaskForm, self).__init__(*args, **kwargs)
        # Фильтруем объект запроса 
        self.fields['taskblock'].queryset = TaskBlock.objects.filter(user=self.user)

class TaskBlockForm(forms.ModelForm):
    "Форма для создания блока задач и обновления параметров блока"
    class Meta:
        model = TaskBlock
        fields = ['title']