from rest_framework import viewsets, views
from rest_framework.response import Response
from core.models import Todo
from core_api.serializers import TodoSerializer


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

