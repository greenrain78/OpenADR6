# Generated by Django 3.2.4 on 2021-08-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_collect', '0003_alter_power_info_perf_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='power_update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.CharField(max_length=50)),
                ('ymdms', models.CharField(max_length=50)),
                ('is_updated', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
