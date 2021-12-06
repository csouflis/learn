from django.urls import path

from cars_fbv import views

app_name = 'cars_fbv'

urlpatterns = [
  path('', views.car_list, name='car_list'),
  path('new/', views.car_create, name='car_new'),
  path('edit/<int:pk>/', views.car_update, name='car_edit'),
  path('delete/<int:pk>/', views.car_delete, name='car_delete'),
]