# Generated by Django 3.0.3 on 2020-11-27 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20200506_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='portal_id',
            field=models.CharField(max_length=30),
        ),
    ]
