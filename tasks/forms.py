from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Task, TaskBlock
import re
import datetime

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

    def clean_deadline(self):
        "Валидация даты"
        deadline = self.cleaned_data['deadline']
        if deadline < datetime.date.today():
            raise ValidationError('Введите дату, начиная с сегодняшней')
        return deadline

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
    """Форма для регистрации пользователя. UserCreationForm - оптимизированная для регистрации версия ModelForm.
    С ней автоматически добавляется логика для: 1) проверки совпадения паролей; 2) хэширования пароля;
    3) проверки уникальности имени пользователя; 4) поля 'password1' и 'password2'."""
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserNameForm(forms.ModelForm):
    "Форма для изменения имени пользователя"
    class Meta:
        model = User
        fields = ['username']

    def clean_username(self):
        """Валидация поля username. Необходима потому, что, несмотря на вывод в форме сообщений об ошибках,
        выполняется сохранение невалидных даннаых """
        username = self.cleaned_data['username']
        # Проверяем, занято ли введённое имя пользователя
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise ValidationError('Это имя пользователя уже занято')
        # Проверяем, содержит ли введённое имя недопустимые символы
        if not re.match(r'^[\w@.+-_]+$', username):
            raise ValidationError('Имя пользователя может содержать только буквы, цифры и символы @/./+/-/_')
        return username
