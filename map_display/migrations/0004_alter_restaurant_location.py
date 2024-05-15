# Generated by Django 3.2 on 2024-05-06 13:22

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map_display', '0003_alter_restaurant_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]