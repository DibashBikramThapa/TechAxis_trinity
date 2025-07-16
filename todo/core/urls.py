from django.urls import path
from core.views import TodoListView, TodoCreateView, TodoDetailView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('create', TodoCreateView.as_view(), name='todo_create'),
    path('detail/<int:pk>', TodoDetailView.as_view(), name='todo_detail'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name='todo_update'),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name='todo_delete'),
]
