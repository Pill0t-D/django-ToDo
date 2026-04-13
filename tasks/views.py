from django.shortcuts import render
from .models import Task

def task_list(request):
    """
    Представление для отображения списка всех задач
    """
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }

    return render(request, 'tasks/task_list.html', context)
    