# Generated by Django 3.2.4 on 2021-07-27 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_collect', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipments_info',
            old_name='eqpCode',
            new_name='eqp_code',
        ),
        migrations.RenameField(
            model_name='equipments_info',
            old_name='eqpName',
            new_name='eqp_name',
        ),
        migrations.RenameField(
            model_name='equipments_info',
            old_name='eqpType',
            new_name='eqp_type',
        ),
        migrations.RenameField(
            model_name='equipments_info',
            old_name='perfId',
            new_name='perf_id',
        ),
        migrations.RenameField(
            model_name='equipments_info',
            old_name='siteId',
            new_name='site_id',
        ),
        migrations.RenameField(
            model_name='power_info',
            old_name='accruePower',
            new_name='accrue_power',
        ),
        migrations.RenameField(
            model_name='power_info',
            old_name='amPere',
            new_name='am_pere',
        ),
        migrations.RenameField(
            model_name='power_info',
            old_name='arPower',
            new_name='ar_power',
        ),
        migrations.RenameField(
            model_name='power_info',
            old_name='atvPower',
            new_name='atv_power',
        ),
        migrations.RenameField(
            model_name='power_info',
            old_name='eqpName',
            new_name='eqp_name',
        ),
        migrations.RenameField(
            model_name='power_info',
            old_name='perfId',
            new_name='perf_id',
        ),
        migrations.RenameField(
            model_name='power_info',
            old_name='pnName',
            new_name='pn_name',
        ),
        migrations.RenameField(
            model_name='power_info',
            old_name='pwFactor',
            new_name='pw_factor',
        ),
        migrations.RenameField(
            model_name='power_info',
            old_name='ratPower',
            new_name='rat_power',
        ),
        migrations.RenameField(
            model_name='power_info',
            old_name='siteId',
            new_name='site_id',
        ),
        migrations.RenameField(
            model_name='power_info',
            old_name='volTage',
            new_name='vol_tage',
        ),
        migrations.RenameField(
            model_name='power_info',
            old_name='voltagerS',
            new_name='voltager_s',
        ),
        migrations.RenameField(
            model_name='power_info',
            old_name='voltagesT',
            new_name='voltages_t',
        ),
        migrations.RenameField(
            model_name='power_info',
            old_name='voltagetR',
            new_name='voltaget_r',
        ),
    ]
