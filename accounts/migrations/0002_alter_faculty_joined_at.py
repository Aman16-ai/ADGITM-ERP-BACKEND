# Generated by Django 4.1.7 on 2023-03-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='joined_at',
            field=models.DateField(),
        ),
    ]
