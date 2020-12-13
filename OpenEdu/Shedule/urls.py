from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authViews

urlpatterns = [
    path('student', views.schedule, name='StudentShedule'),
    path('teacher', views.schedulet, name='TeacherShedule'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)