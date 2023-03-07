# Generated by Django 4.1.7 on 2023-03-06 16:41

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('password_changed', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('Manager', 'Manager'), ('Director', 'Director'), ('CEO', 'CEO'), ('Owner', 'Owner'), ('HOD', 'HOD'), ('DI', 'DI'), ('Professor', 'Professor'), ('Assistant Professor', 'Assistant Professor'), ('Student', 'Student')], max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'default_permissions': ('add', 'view', 'change', 'delete'),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('faculty_id', models.CharField(max_length=50)),
                ('department', models.CharField(choices=[('AIML', 'AIML'), ('AIDS', 'AIDS'), ('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('MAE', 'MAE'), ('CIVIL', 'CIVIL'), ('BA-LLB', 'BA-LLB'), ('BBA', 'BBA'), ('MBA', 'MBA')], max_length=80)),
                ('joined_at', models.DateField(auto_now=True)),
                ('salary', models.PositiveIntegerField()),
                ('last_promotion_on', models.DateField(blank=True, null=True)),
                ('experience', models.IntegerField()),
                ('faculty_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_fac', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_sub', to='accounts.faculty')),
            ],
        ),
    ]
