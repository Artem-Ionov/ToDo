from django.urls import path
from .views import task_list, create_task, update_task, delete_task, create_taskblock, update_taskblock, delete_taskblock
from .views import task_archive, task_detail, recover_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', create_task, name='create_task'),
    path('update/<int:id>', update_task, name='update_task'),           # Передаём внутри url идентификатор задачи в функцию
    path('delete/<int:id>', delete_task, name='delete_task'),
    path('create/taskblock/', create_taskblock, name='create_taskblock'),
    path('update/taskblock/<int:id>', update_taskblock, name='update_taskblock'),
    path('delete/taskblock/<int:id>', delete_taskblock, name='delete_taskblock'),
    path('archive/', task_archive, name='task_archive'),
    path('detail/<int:id>', task_detail, name='task_detail'),
    path('recover/<int:id>', recover_task, name='recover_task'),
]