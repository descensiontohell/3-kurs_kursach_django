# Generated by Django 4.0 on 2021-12-23 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0020_pending_is_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pending',
            name='IS_FINISHED',
        ),
    ]
