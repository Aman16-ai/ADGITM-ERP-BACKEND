# Generated by Django 4.1.7 on 2023-10-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmenant_managnement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]