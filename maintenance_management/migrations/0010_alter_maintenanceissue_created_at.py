# Generated by Django 4.1.7 on 2023-11-11 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_management', '0009_maintenanceissuecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenanceissue',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
