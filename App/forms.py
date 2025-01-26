from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Task
import datetime

class Update(ModelForm):
    def clean_date(self):
        data=self.cleaned_data['date']
        if data < datetime.date.today():
            raise ValidationError('Укажите дату, начиная с сегодняшней')
        return data
    
    class Meta:
        model=Task
        fields=['date', 'completed']
