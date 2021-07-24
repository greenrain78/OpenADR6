from django.db import models


# Create your models here.
class equipments_info(models.Model):
    siteId = models.CharField(max_length=50)
    perfId = models.SmallIntegerField()

    eqpCode = models.CharField(max_length=200)
    eqpName = models.CharField(max_length=200)
    eqpType = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)


class power_info(models.Model):
    siteId = models.CharField(max_length=50)
    perfId = models.CharField(max_length=50)

    pnName = models.CharField(max_length=50)
    eqpName = models.CharField(max_length=50)
    ymdms = models.CharField(max_length=50)

    volTage = models.CharField(max_length=50)
    amPere = models.CharField(max_length=50)
    arPower = models.CharField(max_length=50)
    atvPower = models.CharField(max_length=50)
    ratPower = models.CharField(max_length=50)
    pwFactor = models.CharField(max_length=50)
    accruePower = models.CharField(max_length=50)
    voltagerS = models.CharField(max_length=50)
    voltagesT = models.CharField(max_length=50)
    voltagetR = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

