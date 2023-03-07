# Generated by Django 4.1.7 on 2023-03-07 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_delete_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_sub', to='accounts.faculty')),
            ],
        ),
    ]