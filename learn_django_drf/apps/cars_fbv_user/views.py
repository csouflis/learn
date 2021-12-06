from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Car

class carForm(ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'mileage']

@login_required
def car_list(request, template_name='cars_fbv_user/car_list.html'):
    if request.user.is_superuser:
        car = Car.objects.all()
    else:
        car = Car.objects.filter(user=request.user)
    data = {}
    data['object_list'] = car
    return render(request, template_name, data)

@login_required
def car_create(request, template_name='cars_fbv_user/car_form.html'):
    form = carForm(request.POST or None)
    if form.is_valid():
        car = form.save(commit=False)
        car.user = request.user
        car.save()
        return redirect('cars_fbv_user:car_list')
    return render(request, template_name, {'form':form})

@login_required
def car_update(request, pk, template_name='cars_fbv_user/car_form.html'):
    if request.user.is_superuser:
        car = get_object_or_404(Car, pk=pk)
    else:
        car = get_object_or_404(Car, pk=pk, user=request.user)
    form = carForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('cars_fbv_user:car_list')
    return render(request, template_name, {'form':form})

@login_required
def car_delete(request, pk, template_name='cars_fbv_user/car_confirm_delete.html'):
    if request.user.is_superuser:
        car = get_object_or_404(Car, pk=pk)
    else:
        car = get_object_or_404(Car, pk=pk, user=request.user)
    if request.method=='POST':
        car.delete()
        return redirect('cars_fbv_user:car_list')
    return render(request, template_name, {'object':car})
