from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authViews

urlpatterns = [
    #path('mains/', views.core, name='core'),
    path('', views.core, name='core'),
    path('mains/detail/<int:id>', views.detail, name='detail'),
    url(r'^login/$', views.user_login, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('', views.redir, name='redir'),
    path('profile', views.profile, name='profile'),
    path('schedule', views.schedule, name='schedule'),
    path('schedulet', views.schedulet, name='schedulet'),
    path('gradebook/', views.gradebookhub, name ='gradebookhub'),
    path('gradebook/<int:id>', views.gradebook, name='gradebook')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
