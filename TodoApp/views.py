#from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from TodoApp.models import Task
#from django.shortcuts import HttpResponse
#from django.shortcuts import HttpResponse
# Create your views here.
def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks= Task.objects.filter(is_completed=True)
    print(completed_tasks)
    return render(request, 'TodoApp/home.html',{'tasks':tasks,'completed_tasks':completed_tasks})

def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')
 
def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method=='POST':
        new_task= request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        return render(request, 'TodoApp/edit.html',{'get_task':get_task})

def delete_data(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

