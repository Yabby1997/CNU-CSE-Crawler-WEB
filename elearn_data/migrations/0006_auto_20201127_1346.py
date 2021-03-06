# Generated by Django 3.0.3 on 2020-11-27 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearn_data', '0005_auto_20200429_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elearndata',
            name='report0',
        ),
        migrations.RemoveField(
            model_name='elearndata',
            name='report1',
        ),
        migrations.RemoveField(
            model_name='elearndata',
            name='reports2do',
        ),
        migrations.RemoveField(
            model_name='elearndata',
            name='video0',
        ),
        migrations.RemoveField(
            model_name='elearndata',
            name='video1',
        ),
        migrations.RemoveField(
            model_name='elearndata',
            name='video2',
        ),
        migrations.RemoveField(
            model_name='elearndata',
            name='video3',
        ),
        migrations.RemoveField(
            model_name='elearndata',
            name='video4',
        ),
        migrations.RemoveField(
            model_name='elearndata',
            name='videos2watch',
        ),
        migrations.AddField(
            model_name='elearndata',
            name='materials',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='elearndata',
            name='notices',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='elearndata',
            name='reports',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='elearndata',
            name='reportsDetail',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='elearndata',
            name='videos',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='elearndata',
            name='videosDetail',
            field=models.TextField(default=''),
        ),
    ]
