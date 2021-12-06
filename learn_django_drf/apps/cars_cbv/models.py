from django.db import models
from django.urls import reverse
import datetime

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField(('year'), choices=year_choices(), default=current_year())
    mileage = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cars_cbv:car_edit', kwargs={'pk': self.pk})