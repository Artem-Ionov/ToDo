from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Task, TaskBlock
import datetime

class TaskUpdate(ModelForm):
    def clean_date(self):
        data=self.cleaned_data['date']
        if data and data < datetime.date.today():
            raise ValidationError('Укажите дату, начиная с сегодняшней')
        return data
    
    class Meta:
        model=Task
        fields=['importance', 'date', 'completed']


class TaskAdd(ModelForm):
    def clean_date(self):
        data=self.cleaned_data['date']
        if data and data < datetime.date.today():
            raise ValidationError('Укажите дату, начиная с сегодняшней')
        return data
    
    class Meta:
        model=Task
        fields='__all__'


class TaskBlockAdd(ModelForm):
    class Meta:
        model=TaskBlock
        fields='__all__'
