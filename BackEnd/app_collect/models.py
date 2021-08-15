from django.db import models


# Create your models here.
class equipments_info(models.Model):
    site_id = models.CharField(max_length=50)
    perf_id = models.SmallIntegerField()

    eqp_code = models.CharField(max_length=200)
    eqp_name = models.CharField(max_length=200)
    eqp_type = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)


class power_info(models.Model):
    site_id = models.CharField(max_length=50)
    perf_id = models.SmallIntegerField()

    pn_name = models.CharField(max_length=50)
    eqp_name = models.CharField(max_length=50)
    ymdms = models.DateTimeField()

    vol_tage = models.FloatField()
    am_pere = models.FloatField()
    ar_power = models.FloatField()
    atv_power = models.FloatField()
    rat_power = models.FloatField()
    pw_factor = models.FloatField()
    accrue_power = models.FloatField()
    voltager_s = models.FloatField()
    voltages_t = models.FloatField()
    voltaget_r = models.FloatField()
    temperature = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)


class power_update(models.Model):
    site_id = models.CharField(max_length=50)
    ymdms = models.CharField(max_length=50)
    is_updated = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
