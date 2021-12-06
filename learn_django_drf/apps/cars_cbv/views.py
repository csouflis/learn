from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Car

class carList(ListView):
    model = Car

class carCreate(CreateView):
    model = Car
    fields = ['name', 'pages']
    success_url = reverse_lazy('cars_cbv:car_list')

class carUpdate(UpdateView):
    model = Car
    fields = ['name', 'pages']
    success_url = reverse_lazy('cars_cbv:car_list')

class carDelete(DeleteView):
    model = Car
    success_url = reverse_lazy('cars_cbv:car_list')