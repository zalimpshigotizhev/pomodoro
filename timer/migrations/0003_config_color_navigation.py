# Generated by Django 4.2.6 on 2023-12-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0002_config_alter_pomodor_options_alter_theme_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='color_navigation',
            field=models.CharField(default='#9da1aa', max_length=7, verbose_name='Цвет'),
        ),
    ]
