from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from cars_gcbv_user.models import Car
from cars_gcbv_user.serializers import CarSerializer
from rest_framework import generics


class carList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class carDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer