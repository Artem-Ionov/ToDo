from django.urls import path
from .views import task_list, task_update, task_add, task_delete, question_list, question_detail, question_update 
from .views import question_delete, question_add, question_block_delete

urlpatterns=[
    path('tasks/', task_list, name='task_list'),
    path('tasks/update/<int:pk>', task_update, name='task_update'),
    path('tasks/add/', task_add, name='task_add'),
    path('tasks/delete/<int:pk>', task_delete, name='task_delete'),
    path('questions/', question_list, name='question_list'),
    path('questions/detail/<int:pk>', question_detail, name='question_detail'),
    path('questions/update/<int:pk>', question_update, name='question_update'),
    path('questions/delete/<int:pk>', question_delete, name='question_delete'),
    path('questions/add/', question_add, name='question_add'),
    path('questions_block/delete/<int:pk>', question_block_delete, name='question_block_delete'),
]