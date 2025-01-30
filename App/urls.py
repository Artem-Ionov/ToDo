from django.urls import path
from .views import task_list, task_update, task_add, task_delete

urlpatterns=[
    path('', task_list, name='task_list'),
    path('update/<int:pk>', task_update, name='task_update'),
    path('add/', task_add, name='task_add'),
    path('delete/<int:pk>', task_delete, name='task_delete'),
]