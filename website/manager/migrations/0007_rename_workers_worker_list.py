# Generated by Django 4.0 on 2021-12-22 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_alter_workers_type_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='workers',
            new_name='worker_list',
        ),
    ]