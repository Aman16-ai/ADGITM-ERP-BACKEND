# Generated by Django 4.1.7 on 2023-10-25 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_management', '0007_alter_maintenanceissue_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maintenanceissue',
            old_name='timestamp',
            new_name='created_at',
        ),
    ]