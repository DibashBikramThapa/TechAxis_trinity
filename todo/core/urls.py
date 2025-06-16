from django.urls import path
from core.views import TodoListView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
]
