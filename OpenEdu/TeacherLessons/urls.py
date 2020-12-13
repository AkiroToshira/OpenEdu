from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authViews

urlpatterns = [
    path('lesson/<int:id>', views.lessont, name='TeacherLesson'),
    path('lesson/delete/<int:id>', views.deletechapter, name='DeleteChapter'),
    path('', views.lessonst, name='TeacherLessons'),
    path('lesson/editchapter/<int:id>', views.editchapter, name='EditChapter'),
    path('editdeadline/<int:id>', views.editdeadline, name='EditDeadline'),
    path('deletedeadlines/<int:id>', views.deletedeadlines, name='DeleteDeadline'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
