from django.urls import path

from . import views

urlpatterns = [
    path('student/', views.StudentLessonListViewSet.as_view({'get': 'list'})),
    path('teacher/', views.TeacherLessonListViewSet.as_view({'get': 'list'})),
    path('student/<int:pk>', views.StudentLessonListViewSet.as_view({'get': 'retrieve'})),
    path('teacher/<int:pk>', views.TeacherLessonListViewSet.as_view({'get': 'retrieve'})),
    path('chapter/create/', views.ChapterViewSet.as_view({'post': 'create'})),
    path('chapter/update/<int:pk>', views.ChapterViewSet.as_view({'put': 'update'})),
    path('chapter/delete/<int:pk>', views.ChapterViewSet.as_view({'delete': 'delete'})),
    path('document/add/', views.DocumentViewSet.as_view({'post': 'create'})),
    path('document/delete/', views.DocumentViewSet.as_view({'delete': 'delete'})),
]
