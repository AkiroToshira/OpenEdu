from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ArticleViewSet.as_view({'get': 'list'})),
    path('<int:pk>', views.ArticleViewSet.as_view({'get': 'retrieve'})),
]
