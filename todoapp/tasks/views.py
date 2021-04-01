from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView

from tasks.forms import AddTaskForm, TodoItemForm
from tasks.models import TodoItem

# Create your views here.


def index(request):
    return HttpResponse('Примитивный ответ из приложения tasks')


def complete_task(request, uid):
    print(uid)
    return HttpResponse('OK')


def add_task(request):
    if request.method == 'POST':
        desc = request.POST['description']
        t = TodoItem(description=desc)
        t.save()
    return redirect('/tasks/list')


def delete_task(request, uid):
    print(uid)
    return redirect('/tasks/list')


class TaskListView(ListView):
    queryset = TodoItem.objects.all()
    context_object_name = 'tasks'
    template_name = 'tasks/list.html'


class TaskCreateView(View):
    def my_render(self, request, form):
        return render(request, 'tasks/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasks/list')

        return self.my_render(request, form)

    def get(self, request, *args, **kwargs):
        form = TodoItemForm()
        return self.my_render(request, form)
