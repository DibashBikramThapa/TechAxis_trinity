from django.shortcuts import render
from rest_framework import viewsets, views, response, status
from core.models import Todo
from core_api.serializers import TodoSerializer


class TestApiView(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

