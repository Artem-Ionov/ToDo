from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Task, TaskBlock

class TaskForm(forms.ModelForm):                  # Используем для формы поля из модели
    "Форма для создания задачи и обновления параметров задачи"
    class Meta:
        model = Task
        exclude = ['archive', 'archive_date']     # Используем все поля кроме указанных

    def __init__(self, *args, **kwargs):
        "Редактируем конструктор, чтобы в форме для задачи выводились только блоки задач текущего пользователя"
        # Извлекаем пользователя из списка входных именованных аргументов (с удалением - чтобы не передавать в суперкласс)
        self.user = kwargs.pop('user')  
        # Вызываем конструктор суперкласса - именно в нём происходит формирование полей формы    
        super(TaskForm, self).__init__(*args, **kwargs)
        # Фильтруем объект запроса 
        self.fields['taskblock'].queryset = TaskBlock.objects.filter(user=self.user)

    def clean_completed(self):
        "Функция для валидации поля 'завершено' при нажатии кнопки 'переместить в рахив'"
        completed = self.cleaned_data['completed']
        # Если completed=False и данные формы содержат 'move_in_archive' (информация о нажатой кнопке), возбуждаем исключение
        if not completed and 'move_in_archive' in self.data: 
            raise ValidationError('Нельзя переместить в архив незавершённую задачу')
        return completed


class TaskBlockForm(forms.ModelForm):
    "Форма для создания блока задач и обновления параметров блока"
    class Meta:
        model = TaskBlock
        fields = ['title']                  # Используем поле "название"


class SignUpForm(UserCreationForm):
    "Форма для регистрации пользователя"
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']