from django.shortcuts import render, redirect
from .models import Task, Question, Question_block
from .forms import Task_update, Task_add, Question_update, Question_add

def task_list(request):
    tasks=Task.objects.all()
    return render(request, 'task_list.html', {'tasks':tasks})

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

def question_list(request):
    blocks=Question_block.objects.all()
    return render(request, 'question_list.html', {'blocks':blocks})

def question_detail(request, pk):
    question=Question.objects.get(pk=pk)
    return render(request, 'question_detail.html', {'question': question})

def question_update(request, pk):
    question=Question.objects.get(pk=pk)
    if request.method=='POST':
        form=Question_update(request.POST, instance=question)
        form.save()
        return redirect('question_detail', question.id)
    else:
        form=Question_update()
    return render(request, 'question_update.html', {'form': form, 'question':question})

def question_add(request):
    if request.method=='POST':
        form=Question_add(request.POST)
        form.save()
        return redirect('question_list')
    else:
        form=Question_add()
    return render(request, 'question_add.html', {'form':form})

def question_delete(request, pk):
    question=Question.objects.get(pk=pk)
    question.delete()
    return redirect('question_list')

def question_block_delete(request, pk):
    question_block=Question_block.objects.get(pk=pk)
    question_block.delete()
    return redirect('question_list')






    