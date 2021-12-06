from django.db import models
from django.urls import reverse
from django.conf import settings
import datetime

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class Car(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField(('year'), choices=year_choices(), default=current_year())
    mileage = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cars_fbv_user:car_edit', kwargs={'pk': self.pk})