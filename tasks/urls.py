from django.urls import path
from .views import task_list, update_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('update/<int:id>', update_task, name='update_task')    # Передаём внутри url идентификатор задачи в функцию
]