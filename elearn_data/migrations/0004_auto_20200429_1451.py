# Generated by Django 3.0.3 on 2020-04-29 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearn_data', '0003_auto_20200429_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elearndata',
            name='report2',
        ),
        migrations.RemoveField(
            model_name='elearndata',
            name='video5',
        ),
    ]
