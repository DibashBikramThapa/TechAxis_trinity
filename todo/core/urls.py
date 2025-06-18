from django.urls import path
from core.views import TodoListView, TodoCreateView, TodoDetailView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('create', TodoCreateView.as_view(), name='todo_create'),
    path('detail/<int:pk>', TodoDetailView.as_view(), name='todo_detail'),
]
