from django.http import HttpResponse
from django.shortcuts import render
from tasks.models import TodoItem

# Create your views here.


def index(request):
    return HttpResponse('Примитивный ответ из приложения tasks')


def tasks_list(request):
    all_tasks = TodoItem.objects.all()
    return render(
        request,
        'tasks/list.html',
        {'tasks': all_tasks}
    )