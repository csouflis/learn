from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Car

class carForm(ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'mileage']

def car_list(request, template_name='cars_fbv/car_list.html'):
    car = Car.objects.all()
    data = {}
    data['object_list'] = car
    return render(request, template_name, data)

def car_create(request, template_name='cars_fbv/car_form.html'):
    form = carForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cars_fbv:car_list')
    return render(request, template_name, {'form': form})

def car_update(request, pk, template_name='cars_fbv/car_form.html'):
    car= get_object_or_404(Car, pk=pk)
    form = carForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('cars_fbv:car_list')
    return render(request, template_name, {'form': form})

def car_delete(request, pk, template_name='cars_fbv/car_confirm_delete.html'):
    car= get_object_or_404(Car, pk=pk)    
    if request.method=='POST':
        car.delete()
        return redirect('cars_fbv:car_list')
    return render(request, template_name, {'object': Car})
