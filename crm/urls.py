from django.urls import path

from . import views

app_name = 'crm'

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('<int:id>/<slug:client>/', views.client_detail, name='client_detail'),
]
