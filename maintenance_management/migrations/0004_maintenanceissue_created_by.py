# Generated by Django 4.1.7 on 2023-10-18 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maintenance_management', '0003_alter_maintenanceissue_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenanceissue',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]