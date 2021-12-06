from django.urls import path
from cars_gcbv_user import views

app_name = 'cars_gcbv_user'

urlpatterns = [
  path('', views.carList.as_view(), name='car_list'),
  path('edit/<int:pk>/', views.carDetail.as_view(), name='car_edit'),
  path('delete/<int:pk>/', views.carDetail.as_view(), name='car_delete'),
]