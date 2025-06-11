from django.shortcuts import render, redirect
from .models import Task, TaskBlock
from .forms import UpdateForm

def task_list(request):
    "Получение всех блоков задач (задачи для каждого блока выводятся в шаблоне)"
    blocks = TaskBlock.objects.all()
    return render(request, 'task_list.html', {'blocks': blocks})

def update_task(request, id):
    "Обновление параметров задачи"
    task = Task.objects.get(pk=id)                      # Получение экземпляра задачи по принятому идентификатору
    if request.method == "POST":                        # Если поступает POST-запрос,
        form = UpdateForm(request.POST, instance=task)
        if form.is_valid():                             # выполняем валидацию данных и, в случае успеха, 
            form.save()                                 # сохраняем объект с изменёнными параметрами в базу,
            return redirect('task_list')                # после чего перенаправляем на страницу со списком задач
    else:                                               # В протвином случае
        form = UpdateForm(instance=task)                # выводим форму с сохранёнными на текущий момент данными
    return render(request, 'update_task.html', {'form': form, 'task': task})

def delete_task(request, id):
    "Удаление задачи"
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('task_list')

def create_task(request):
    "Создание новой задачи"
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = UpdateForm()
    return render(request, 'create_task.html', {'form': form})
