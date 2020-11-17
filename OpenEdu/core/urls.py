from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.core, name="core"),
    path('detail/<int:id>', views.detail, name="detail"),
    url(r'^login/$', views.user_login, name='login'),
    path('logout', views.user_logout.as_view(), name='logout')
]
