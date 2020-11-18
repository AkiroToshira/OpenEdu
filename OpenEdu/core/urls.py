from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('mains/', views.core, name="core"),
    path('detail/<int:id>', views.detail, name="detail"),
    url(r'^login/$', views.user_login, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('lessons/', views.lessons,name="lessons")
]