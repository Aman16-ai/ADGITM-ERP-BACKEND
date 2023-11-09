# Generated by Django 4.1.7 on 2023-11-09 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maintenance_management', '0008_rename_timestamp_maintenanceissue_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceIssueComment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('maintenanceIssue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance_management.maintenanceissue')),
            ],
        ),
    ]
