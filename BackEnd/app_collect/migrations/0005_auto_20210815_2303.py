# Generated by Django 3.2.4 on 2021-08-15 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_collect', '0004_power_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='power_info',
            name='accrue_power',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='power_info',
            name='am_pere',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='power_info',
            name='ar_power',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='power_info',
            name='atv_power',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='power_info',
            name='pw_factor',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='power_info',
            name='rat_power',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='power_info',
            name='temperature',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='power_info',
            name='vol_tage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='power_info',
            name='voltager_s',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='power_info',
            name='voltages_t',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='power_info',
            name='voltaget_r',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='power_info',
            name='ymdms',
            field=models.DateTimeField(),
        ),
    ]
