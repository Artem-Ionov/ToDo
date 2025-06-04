from django.shortcuts import render, redirect
from .models import Task
from .forms import UpdateForm

def task_list(request):
    "Получение списка текущих задач"
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

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
    return render(request, 'update_task.html', {'form': form})