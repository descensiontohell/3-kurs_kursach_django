# Generated by Django 4.0 on 2021-12-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0013_alter_bought_parts_car_id_alter_parts_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bought_parts',
            name='CAR_ID',
            field=models.IntegerField(default=0),
        ),
    ]