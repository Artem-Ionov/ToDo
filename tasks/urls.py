from django.urls import path
from .views import task_list, update_task, delete_task, create_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('update/<int:id>', update_task, name='update_task'),    # Передаём внутри url идентификатор задачи в функцию
    path('delete/<int:id>', delete_task, name='delete_task'),
    path('create/', create_task, name='create_task'),
]