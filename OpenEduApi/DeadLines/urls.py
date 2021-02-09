from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    path('', views.DeadlinesViewSet.as_view({'get': 'list'})),
    path('create', views.DeadlinesViewSet.as_view({'post': 'create'})),
    path('update', views.DeadlinesViewSet.as_view({'put': 'update'})),
    path('delete', views.DeadlinesViewSet.as_view({'delete': 'delete'})),
])

