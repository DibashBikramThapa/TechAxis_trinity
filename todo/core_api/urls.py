from django.urls import path, include
from core_api.views import TestApiView

urlpatterns = [
    path('todo/', include([
            path('', TestApiView.as_view({'get': 'list', 'post': 'create'})),
        ])
    )
]
