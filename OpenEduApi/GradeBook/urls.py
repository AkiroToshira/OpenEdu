from django.urls import path

from . import views

urlpatterns = [
    path('teacher/<int:pk>', views.TeacherGradeBookViewSet.as_view({'get': 'retrieve'})),
    path('teacher/grade', views.GradeViewSet.as_view({'put': 'update'}))
]