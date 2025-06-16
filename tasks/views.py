from django.shortcuts import render, redirect
from .models import Task, TaskBlock
from .forms import TaskForm, TaskBlockForm

def task_list(request):
    "Получение блоков задач текущего пользователя (задачи для каждого блока выводятся в шаблоне)"
    if request.user.is_authenticated:                               # Если пользователь аутентифицирован,
        taskblocks = TaskBlock.objects.filter(user=request.user)    # получаем его блоки задач
        return render(request, 'task_list.html', {'taskblocks': taskblocks})
    else:                                                           # Если нет, перенаправляем на страницу входа
        return redirect('login')

def create_task(request):
    "Создание новой задачи"
    if request.method == 'POST':                          # Если поступает POST-запрос,
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():                               # выполняем валидацию данных и, в случае успеха, 
            form.save()                                   # сохраняем объект в базу,
            return redirect('task_list')                  # после чего перенаправляем на страницу со списком задач
    else:                                                 # В протвином случае
        form = TaskForm(user=request.user)                # выводим форму с пустыми полями для заполнения
    return render(request, 'create_task.html', {'form': form})

def update_task(request, id):
    "Обновление параметров задачи"
    task = Task.objects.get(pk=id)                        # Получение экземпляра задачи по принятому идентификатору
    if request.method == "POST":                          # Передаём в форму экземпляр задачи и текущего пользователя
        form = TaskForm(request.POST, instance=task, user=request.user) 
        if form.is_valid():                               
            form.save()                                   
            return redirect('task_list')                  
    else:                                                 
        form = TaskForm(instance=task, user=request.user) # Форма выводится со значениями, взятыми из базы
    return render(request, 'update_task.html', {'form': form, 'task': task})

def delete_task(request, id):
    "Удаление задачи"
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('task_list')

def create_taskblock(request):
    "Создание нового блока задач"
    if request.method == 'POST':
        form = TaskBlockForm(request.POST)
        if form.is_valid():
            taskblock = form.save(commit=False)         # Создаём экземпляр блока задач, но не сохраняем его, чтобы
            taskblock.user = request.user               # автоматически добавить текущего пользователя как автора блока  
            taskblock.save()
            return redirect('task_list')
    else:
        form = TaskBlockForm()
    return render(request, 'create_taskblock.html', {'form': form})

def update_taskblock(request, id):
    "Обновление параметров блока задач"
    taskblock = TaskBlock.objects.get(pk=id)
    if request.method == 'POST':
        form = TaskBlockForm(request.POST, instance=taskblock)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskBlockForm(instance=taskblock)
    return render(request, 'update_taskblock.html', {'form': form, 'taskblock': taskblock})

def delete_taskblock(request, id):
    "Удаление блока задач"
    taskblock = TaskBlock.objects.get(pk=id)
    taskblock.delete()
    return redirect('task_list')