# Generated by Django 4.0 on 2021-12-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_finished_works_id_alter_finished_works_ticket_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bought_parts',
            name='CAR_ID',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='parts',
            name='CAR_ID',
            field=models.IntegerField(default=0),
        ),
    ]