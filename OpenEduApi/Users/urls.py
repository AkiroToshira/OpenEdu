from django.urls import path, include

from . import views

urlpatterns = [
    path('<int:pk>', views.UserViewSet.as_view({'get': 'retrieve'})),
    path('react-info/', views.UserViewSetReact.as_view({'get': 'retrieve'})),
    path('groups/create/', views.GroupViewSet.as_view({'post': 'create'})),
    path('groups/delete/<int:pk>', views.GroupViewSet.as_view({'delete': 'delete'})),
    path('groups/list/', views.GroupViewSet.as_view({'get': 'list'})),
    path('groups/addstudent/<int:pk>', views.GroupViewSet.as_view({'post': 'add_student'})),
    path('groups/removestudent/<int:pk>', views.GroupViewSet.as_view({'post': 'remove_student'})),
    path('register/', views.RegisterViewSet.as_view({'post': 'create'})),
]
