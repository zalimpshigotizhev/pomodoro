# Generated by Django 3.2.23 on 2023-12-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0009_auto_20231228_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='song_intensive',
            field=models.CharField(default='/melody/matrix.mp3', max_length=100, verbose_name='URL к мелодии'),
        ),
        migrations.AlterField(
            model_name='config',
            name='song_relax',
            field=models.CharField(default='/melody/matrix.mp3', max_length=100, verbose_name='URL к мелодии'),
        ),
    ]