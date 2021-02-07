from django.urls import path

from . import views

urlpatterns = [
    path('', views.DeadlinesViewSet.as_view({'get': 'list'})),
]

