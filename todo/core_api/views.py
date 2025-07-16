from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from django.db.models import Q

from core.models import Todo
from core_api.serializers import TodoSerializer, TodoCreateSerializer
from auth_api.authentication import CustomTokenAuth


class MyCustomView(views.APIView):

    def get(self, request, format=None):
            """
            Return a msg.
            """
            data = {
                "message": "I am from custom"
            }
            return Response(data)

    def post(self, request, format=None):
         user = request.data.get("user")
         data = {
              "message": f"{user} have submitted data"
         }
         return Response(data)


class TodoApiView(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset =  super().get_queryset()
        my_filter = Q()
        query = self.request.GET.get('q')
        if not self.request.user.is_superuser:
            my_filter &= Q(created_by=self.request.user)
        if query:
            query = query.strip()
            my_filter &= (Q(name__contains=query) | Q(description__contains=query))
        queryset = queryset.filter(my_filter)
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            serializer = super().get_serializer_class()
        else:
             serializer = TodoCreateSerializer
        return serializer
