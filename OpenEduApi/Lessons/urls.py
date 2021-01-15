from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.LessonViewSet.as_view({'get': 'list'})),
    path('student', views.StudentLessonListViewSet.as_view({'get': 'list'})),
    path('teacher', views.TeacherLessonListViewSet.as_view({'get': 'list'})),
]
