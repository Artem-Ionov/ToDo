from django.urls import path
from .views import task_list, task_update, task_add, task_delete, task_block_add, task_block_delete

urlpatterns=[
    path('tasks/', task_list, name='task_list'),
    path('tasks/update/<int:pk>', task_update, name='task_update'),
    path('tasks/add/', task_add, name='task_add'),
    path('tasks/delete/<int:pk>', task_delete, name='task_delete'),
    path('tasks/taskblock/add/', task_block_add, name='task_block_add'),
    path('tasks/taskblock/delete/<int:pk>', task_block_delete, name='task_block_delete'),
]