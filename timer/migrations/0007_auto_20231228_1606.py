# Generated by Django 3.2.23 on 2023-12-28 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0006_song_pomodorconfig_time_relax_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pomodorconfig',
            name='song_intensive',
        ),
        migrations.RemoveField(
            model_name='pomodorconfig',
            name='song_relax',
        ),
        migrations.AddField(
            model_name='config',
            name='song_intensive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='config_intensive', to='timer.song'),
        ),
        migrations.AddField(
            model_name='config',
            name='song_relax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='config_relax', to='timer.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='url',
            field=models.CharField(max_length=200, verbose_name='Расположение мелодии'),
        ),
    ]
