from django.urls import path, include

from . import views

urlpatterns = [
    path('<int:pk>', views.UserViewSet.as_view({'get': 'retrieve'})),
    path('react-info/', views.UserViewSetReact.as_view({'get': 'retrieve'})),
]
