from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from core.models import Todo
from core.forms import TodoCreateForm


class TodoListView(LoginRequiredMixin, generic.ListView):
    queryset = Todo.objects.all()
    template_name = 'core/list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        queryset =  super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            my_filter = Q(name__contains=query) | Q(description__contains=query)
            queryset = queryset.filter(my_filter)
        return queryset


class TodoCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'core/create.html'
    form_class = TodoCreateForm
    success_url = reverse_lazy('todo_list')


class TodoDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'core/detail.html'
    queryset = Todo.objects.all()
    context_object_name = 'todo'


class TodoUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'core/update.html'
    form_class = TodoCreateForm
    queryset = Todo.objects.all()
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'core/delete.html'
    queryset = Todo.objects.all()
    success_url = reverse_lazy('todo_list')