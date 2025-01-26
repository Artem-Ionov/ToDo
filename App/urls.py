from django.urls import path
from .views import task_list, task_update, task_add

urlpatterns=[
    path('', task_list, name='task_list'),
    path('update/<int:pk>', task_update, name='task_update'),
    path('add/', task_add, name='task_add'),
]