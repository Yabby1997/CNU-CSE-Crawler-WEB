# Generated by Django 3.0.3 on 2020-05-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20200430_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='portal_pw',
            field=models.CharField(max_length=300),
        ),
    ]
