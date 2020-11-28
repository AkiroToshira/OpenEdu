from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authViews

urlpatterns = [
]
urlpatterns = [
    path('mains/', views.core, name='core'),
    path('mains/detail/<int:id>', views.detail, name='detail'),
    url(r'^login/$', views.user_login, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('lessons/', views.lessons, name='lessons'),
    path('lessons/lesson/<int:id>', views.lesson, name='lesson'),
    path('', views.redir, name='redir'),
    path('mains/profile', views.profile, name='profile'),
    path('schedule', views.schedule, name='schedule'),
    path('lessont/lesson/<int:id>', views.lessont, name='lessont'),
    path('lessont/lesson/add/<int:id>', views.addchapter, name='addchapter')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
