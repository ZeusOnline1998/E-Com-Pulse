from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.urls.authtoken')),
    path('user_login/', views.user_login, name='user-login'),
    path('get_user_details/', views.get_user_details, name='get-user=details'),
]
