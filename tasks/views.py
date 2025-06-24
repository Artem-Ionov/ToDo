from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Task, TaskBlock
from .forms import TaskForm, TaskBlockForm, SignUpForm, UserNameForm
from datetime import datetime

@login_required                     # Функция требует аутентификации (иначе происходит перенаправление на 'login')
def task_list(request):
    "Получение блоков задач текущего пользователя (задачи для каждого блока выводятся в шаблоне)"
    taskblocks = TaskBlock.objects.filter(user=request.user)  # Получаем блоки задач текущего пользователя
    for taskblock in taskblocks:                              # Для каждого блока фильтруем задачи по полю 'archive',
        taskblock.filtered_tasks = taskblock.task_set.filter(archive=False) # присваивая результат новому атрибуту
    return render(request, 'task_list.html', {'taskblocks': taskblocks})

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
            if 'save' in request.POST:                    # Если в параметрах POST-запроса есть ключ 'save' (поле                
                form.save()                               #  name в форме), сохраняем изменения в базу    
                return redirect('task_list')              # и переходим к списку задач
            elif 'move_in_archive' in request.POST:       # Если же в параметрах POST-запроса есть ключ 'arcive',
                task.archive=True                         # изменяем поле 'archive' на True,
                task.archive_date = datetime.now()        # фиксируем дату архивации,
                task.save()                               # сохраняем
                return redirect('task_archive')           # и переходим в архив       
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
            taskblock = form.save(commit=False)         # Создаём экземпляр блока задач, но не сохраняем его сразу, чтобы
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

@login_required
def task_archive(request):
    "Получение архивных задач"
    # Фильтрация задач по полю 'archive' и сортировка по полю 'archive_date'
    tasks = Task.objects.filter(archive=True).order_by('-archive_date') 
    return render(request, 'task_archive.html', {'tasks': tasks})

def task_detail(request, id):
    "Получение детельной информации о задаче"
    task = Task.objects.get(pk=id)
    return render(request, 'task_detail.html', {'task': task})

def recover_task(request, id):
    "Восстановление задачи из архива"
    task = Task.objects.get(pk=id)
    task.archive = False
    task.save()
    return redirect('task_list')

def sign_up(request):
    "Регистрация пользователя"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)                                # Аутентификация зарегистрированного пользователя
            return redirect('task_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', {'form': form})

@login_required
def settings(request):
    "Настройки пользователя"
    username_form = UserNameForm(instance=request.user)         # Выносим вперёд, чтобы при ошибках валидации 
    password_form = PasswordChangeForm(user=request.user)       # обе переменные передавались в шаблон
    if request.method == 'POST':
        if 'change_username' in request.POST:
            username_form = UserNameForm(request.POST, instance=request.user)
            if username_form.is_valid():
                username_form.save()
                return redirect('settings')
        elif 'change_password' in request.POST:
            """ Форма PasswordChangeForm требует именованных аргументов. Благодаря её использованию автоматически 
            выполняется 1) хэширование пароля; 2) валидация сложности пароля (AUTH_PASSWORD_VALIDATORS из settings.py);
            3) проверка старого пароля; 4) проверка совпадения паролей; 5) форма уже содержит все нужные поля"""
            password_form = PasswordChangeForm(data=request.POST, user=request.user)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)     # Обновляем сессию, чтобы пользователь не разлогинился
                return redirect('settings')
    return render(request, 'settings.html', {'username_form': username_form, 'password_form': password_form})
