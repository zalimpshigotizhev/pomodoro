# Generated by Django 3.2.23 on 2024-01-10 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0015_auto_20240109_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pomodor',
            name='session',
        ),
        migrations.RemoveField(
            model_name='rest',
            name='session',
        ),
        migrations.DeleteModel(
            name='Session',
        ),
    ]