# Generated by Django 3.2.16 on 2022-10-09 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_name_manufacturer_car_manufacturer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='overload_percent',
        ),
    ]
