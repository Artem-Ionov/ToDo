from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Task, Question
import datetime

class Task_update(ModelForm):
    def clean_date(self):
        data=self.cleaned_data['date']
        if data and data < datetime.date.today():
            raise ValidationError('Укажите дату, начиная с сегодняшней')
        return data
    
    class Meta:
        model=Task
        fields=['importance', 'date', 'completed']


class Task_add(ModelForm):
    def clean_date(self):
        data=self.cleaned_data['date']
        if data and data < datetime.date.today():
            raise ValidationError('Укажите дату, начиная с сегодняшней')
        return data
    
    class Meta:
        model=Task
        fields='__all__'


class Question_update(ModelForm):
    class Meta:
        model=Question
        fields=['decision']


class Question_add(ModelForm):
    class Meta:
        model=Question
        fields='__all__'