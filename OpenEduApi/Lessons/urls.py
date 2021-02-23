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
    path('lesson/create/', views.StudentLessonListViewSet.as_view({'post': 'create'})),
    path('lesson/update/<int:pk>', views.StudentLessonListViewSet.as_view({'put': 'update'})),
    path('lesson/delete/<int:pk>', views.StudentLessonListViewSet.as_view({'delete': 'delete'})),
    path('lesson/addmoderator/<int:pk>', views.AdminViewSet.as_view({'post': 'add_moderator'})),
    path('lesson/removemoderator/<int:pk>', views.AdminViewSet.as_view({'post': 'remove_moderator'})),
    #path('lesson/addgroup/<int:pk>', views.AdminViewSet.as_view({'post': 'add_group'})),
    #path('lesson/removegroup/<int:pk>', views.AdminViewSet.as_view({'post': 'remove_group'})),
]
