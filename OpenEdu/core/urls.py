from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('mains/', views.core, name='core'),
    path('mains/detail/<int:id>', views.detail, name='detail'),
    url(r'^login/$', views.user_login, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('lessons/', views.lessons, name='lessons'),
    path('lessons/lesson/<int:id>', views.lesson, name='lesson'),
    path('', views.redir, name='redir'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
