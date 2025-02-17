from django.shortcuts import render, redirect
from .models import Task, TaskBlock
from .forms import TaskUpdate, TaskAdd, TaskBlockAdd

def task_list(request):
    if request.user.is_authenticated:
        blocks=TaskBlock.objects.filter(user=request.user)
        return render(request, 'task_list.html', {'blocks':blocks})
    else:
        return redirect('login')

def task_update(request, pk):
    task=Task.objects.get(pk=pk)
    if request.method=='POST':
        form=TaskUpdate(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=TaskUpdate()
    return render(request, 'task_update.html', {'form': form, 'task': task})

def task_add(request):
    if request.method=='POST':
        form=TaskAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=TaskAdd()
    return render(request, 'task_add.html', {'form': form})

def task_delete(request, pk):
    task=Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')

def task_block_add(request):
    if request.method=='POST':
        form=TaskBlockAdd(request.POST)
        form.save()
        return redirect('task_list')
    else:
        form=TaskBlockAdd()
    return render(request, 'task_block_add.html', {'form':form})

def task_block_delete(request, pk):
    block=TaskBlock.objects.get(pk=pk)
    block.delete()
    return redirect('task_list')







    