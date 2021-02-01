from django.urls import path

from . import views

urlpatterns = [
    path('', views.ScheduleViewSet.as_view({'get': 'list'})),
]
