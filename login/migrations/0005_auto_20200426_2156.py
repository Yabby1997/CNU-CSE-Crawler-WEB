# Generated by Django 3.0.3 on 2020-04-26 12:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20200426_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
