from django.shortcuts import render
from django.views import generic
# Create your views here.

from core.models import Todo


class TodoListView(generic.ListView):
    queryset = Todo.objects.all()
    template_name = 'core/list.html'
    context_object_name = 'todos'


