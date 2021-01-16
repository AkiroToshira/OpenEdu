from django.urls import path, include

from . import views

urlpatterns = [
    path('<int:pk>', views.UserViewSet.as_view({'get': 'retrieve'})),
]
