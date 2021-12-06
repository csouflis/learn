from django.urls import path

from . import views

app_name = 'cars_cbv'

urlpatterns = [
  path('', views.carList.as_view(), name='car_list'),
  path('new/', views.carCreate.as_view(), name='car_new'),
  path('edit/<int:pk>/', views.carUpdate.as_view(), name='car_edit'),
  path('delete/<int:pk>/', views.carDelete.as_view(), name='car_delete'),
]