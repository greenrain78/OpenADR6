from django.db import models


# Create your models here.


# Create your models here.
class predict_atv_power(models.Model):
    site_id = models.CharField(max_length=50)
    perf_id = models.SmallIntegerField()

    ymdms = models.DateTimeField()  # 예측 데이터 목표 날짜
    atv_power = models.FloatField()

    model_name = models.CharField(max_length=50)
    predict_cycle = models.CharField(max_length=50)
    predict_range = models.CharField(max_length=50)
    predict_interval = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)  # 예측 수행 날짜


class predict_dashboard(models.Model):

    site_id = models.CharField(max_length=50)
    perf_id = models.SmallIntegerField()

    predict_atv_power_count = models.IntegerField()

    ymdms = models.DateTimeField()  # 예측 데이터 목표 날짜
    created_at = models.DateTimeField(auto_now_add=True)  # 예측 수행 날짜
