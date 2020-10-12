from django.shortcuts import render,redirect
from django.http import HttpResponse
from todo.models import TaskList
from todo.forms  import TaskForm
from django.contrib import messages

# Create your views here.
def todo(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New task added!!"))
        return redirect('todo')
    else:
        all_tasks = TaskList.objects.all
        return render(request,'todo.html',{'all_task' : all_tasks})

def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    
    return redirect('todo')

def edit_task(request, task_id):
    if request.method == 'POST':
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()


        messages.success(request,("Task edited!!"))
        return redirect("todo")
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj' : task_obj})


def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    
    return redirect('todo')


def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    
    return redirect('todo')