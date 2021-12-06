from rest_framework import serializers
from cars_gcbv_user.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"