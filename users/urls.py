from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.user_login_view, name='login'),
    path('profile/', views.user_profile_view, name='profile'),
]
