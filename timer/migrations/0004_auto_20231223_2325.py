# Generated by Django 3.2.23 on 2023-12-23 20:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0003_config_color_navigation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='color',
            field=models.CharField(default='#9da1aa', max_length=7, verbose_name='Цвет фона'),
        ),
        migrations.AlterField(
            model_name='config',
            name='color_navigation',
            field=models.CharField(default='#9da1aa', max_length=7, verbose_name='Цвет навигации'),
        ),
        migrations.AlterField(
            model_name='pomodor',
            name='datetime_field',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Дата и время создание'),
        ),
        migrations.CreateModel(
            name='PomodorConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_intensive', models.PositiveIntegerField(default=25, verbose_name='Время помидора')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configuration', to='timer.theme', verbose_name='Выбранная тема')),
            ],
        ),
    ]
