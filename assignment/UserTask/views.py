from django.shortcuts import render, redirect
from .forms import UserForm, TaskForm
from .models import User, Task
from django.core.paginator import Paginator
from django.http import HttpResponse
import pandas as pd


def indexView(request):
    return render(request, 'index.html')

def userView(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_list.html")
        else:
            form = UserForm()
        return render(request, "user.html", {'form': form})
    
def taskView(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list.html")
        else:
            form = TaskForm()
        return render(request, "task.html", {'form': form})
    

def userListView(request):
    users = User.objects.all()
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "user_list.html", {'page_obj': page_obj})


def taskListView(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "task_list.html", {'page_obj': page_obj})


def export_to_excel(request):
    users = User.objects.all().values()
    tasks = Task.objects.all().values()
    
    
    user_data = pd.DataFrame(users)
    task_data = pd.DataFrame(tasks)
    
    with pd.ExcelWriter("/mnt/data/user_task.xlsx") as writer:
        user_data.to_excel(writer, sheet_name="Users", index=False)
        task_data.to_excel(writer, sheet_name="Tasks", index=False)
        
    
    response = HttpResponse(open("/mnt/data/user_task.xlsx").read(), content_type="application/vnd.ms-excel")
    response['Content-Disposition'] = 'attachment; filename="user_task.xlsx"'
    
    return response