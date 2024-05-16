# Generated by Django 4.2.1 on 2024-05-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_display', '0025_remove_electricpole_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='electricpole',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='electricpole',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]