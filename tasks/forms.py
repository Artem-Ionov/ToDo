from django import forms
from .models import Task

class UpdateForm(forms.ModelForm):          # Используем для формы поля из модели
    class Meta:
        model = Task
        fields = "__all__"