# Generated by Django 4.1.7 on 2023-10-17 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenanceissue',
            name='timestamp',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]