# Generated by Django 3.2.23 on 2024-01-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0016_auto_20240110_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rest',
            name='icon',
            field=models.CharField(default='🏖️', max_length=10, verbose_name='Иконка'),
        ),
    ]
