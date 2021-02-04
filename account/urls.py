from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile_list, name='profile_list'),
    path('profile/<int:id>/<slug:profile>/',
         views.profile_detail,
         name='profile_detail'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
