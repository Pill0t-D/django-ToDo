from django.shortcuts import render
from .models import Task

def task_list(request):
    """
    View for displaying list of all tasks
    """
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }

    return render(request, 'tasks/task_list.html', context)
    