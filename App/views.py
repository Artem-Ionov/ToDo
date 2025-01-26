from django.shortcuts import render, redirect
from .models import Task
from .forms import Update, Add

def task_list(request):
    tasks=Task.objects.all()
    return render(request, 'task_list.html', {'tasks':tasks})

def task_update(request, pk):
    task=Task.objects.get(pk=pk)
    if request.method=='POST':
        form=Update(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=Update()
    return render(request, 'task_update.html', {'form': form, 'task': task})

def task_add(request):
    if request.method=='POST':
        form=Add(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=Add()
    return render(request, 'task_add.html', {'form': form})