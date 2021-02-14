from django.urls import path

from . import views

urlpatterns = [
    path('teacher/<int:pk>', views.TeacherGradeBookViewSet.as_view({'get': 'retrieve'})),
    path('student/', views.StudentGradeBookViewSet.as_view({'get': 'list'})),
    path('teacher/grade/', views.GradeViewSet.as_view({'put': 'update'})),
    path('gradebooklist/', views.TeacherGradeBookViewSet.as_view({'get': 'grade_book_list'})),
]