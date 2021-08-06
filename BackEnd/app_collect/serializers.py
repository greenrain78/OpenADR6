from rest_framework import serializers
from .models import equipments_info


class EquipmentsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = equipments_info
        fields = '__all__'
