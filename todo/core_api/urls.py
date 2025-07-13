from django.urls import path, include
from core_api.views import TodoApiView, MyCustomView

urlpatterns = [
    path('', MyCustomView.as_view()),
    path('todo/', include([
            path('', TodoApiView.as_view({'get': 'list', 'post': 'create'})),
            path('<int:pk>', TodoApiView.as_view({'get': 'retrieve'})),
        ])
    )
]
