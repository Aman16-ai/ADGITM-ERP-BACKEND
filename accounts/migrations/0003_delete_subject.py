# Generated by Django 4.1.7 on 2023-03-07 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_faculty_joined_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
