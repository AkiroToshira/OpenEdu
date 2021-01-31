from django.urls import path

from . import views

urlpatterns = [
    path('student/', views.ScheduleViewSet.as_view({'get': 'list'})),
]
