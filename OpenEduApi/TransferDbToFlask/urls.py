from django.urls import path

from . import views

urlpatterns = [
    path('simple/<int:pk>', views.CountGradeBookViewSet.as_view({'get': 'simple_count'})),
]
