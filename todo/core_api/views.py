from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from core.models import Todo
from core_api.serializers import TodoSerializer
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

    authentication_classes = [CustomTokenAuth, ]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


    def list(self, request, *args, **kwargs):
         return super().list(request, *args, **kwargs)

