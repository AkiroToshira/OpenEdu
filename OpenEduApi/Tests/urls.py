from django.urls import path

from . import views

urlpatterns = [
    path('lesson/<int:pk>', views.StudentTestViewSet.as_view({'get': 'list'})),
    path('<int:pk>', views.StudentTestViewSet.as_view({'get': 'retrieve'})),
    path('count/<int:pk>', views.StudentTestViewSet.as_view({'post': 'count'})),
]
