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
    ymdms = models.CharField(max_length=50)

    vol_tage = models.CharField(max_length=50)
    am_pere = models.CharField(max_length=50)
    ar_power = models.CharField(max_length=50)
    atv_power = models.CharField(max_length=50)
    rat_power = models.CharField(max_length=50)
    pw_factor = models.CharField(max_length=50)
    accrue_power = models.CharField(max_length=50)
    voltager_s = models.CharField(max_length=50)
    voltages_t = models.CharField(max_length=50)
    voltaget_r = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

