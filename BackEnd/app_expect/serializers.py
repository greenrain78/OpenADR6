from rest_framework import serializers

from app_expect.models import predict_atv_power


class Predict_atv_powerSerializer(serializers.ModelSerializer):
    class Meta:
        model = predict_atv_power
        fields = '__all__'
