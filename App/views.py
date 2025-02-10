from django.shortcuts import render, redirect
from .models import Task, Task_block
from .forms import Task_update, Task_add, Task_block_add

def task_list(request):
    if request.user.is_authenticated:
        blocks=Task_block.objects.filter(user=request.user)
        return render(request, 'task_list.html', {'blocks':blocks})
    else:
        return redirect('login')

def task_update(request, pk):
    task=Task.objects.get(pk=pk)
    if request.method=='POST':
        form=Task_update(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=Task_update()
    return render(request, 'task_update.html', {'form': form, 'task': task})

def task_add(request):
    if request.method=='POST':
        form=Task_add(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=Task_add()
    return render(request, 'task_add.html', {'form': form})

def task_delete(request, pk):
    task=Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')

def task_block_add(request):
    if request.method=='POST':
        form=Task_block_add(request.POST)
        form.save()
        return redirect('task_list')
    else:
        form=Task_block_add()
    return render(request, 'task_block_add.html', {'form':form})

def task_block_delete(request, pk):
    block=Task_block.objects.get(pk=pk)
    block.delete()
    return redirect('task_list')







    