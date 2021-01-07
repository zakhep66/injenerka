# Generated by Django 3.1.2 on 2021-01-06 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serName', models.CharField(max_length=30, verbose_name='Фамилия клиента')),
                ('name', models.CharField(max_length=30, verbose_name='Имя клиента')),
                ('fathName', models.CharField(max_length=30, verbose_name='Отчество клиента')),
                ('tel', models.IntegerField(max_length=11, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=40, verbose_name='Email')),
            ],
        ),
    ]