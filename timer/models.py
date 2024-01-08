from datetime import datetime
from django.db import models
import core

class Theme(models.Model):
    name = models.CharField(
        verbose_name='Название темы',
        max_length=core.MAX_LENGTH_NAME_THEME
    )
    def __str__(self) -> str:
        return self.name
    
    def get_pomodors_count(self):
        return self.pomodors.count()
    
    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"        

class Pomodor(models.Model):
    theme = models.ForeignKey(
        Theme,
        related_name='pomodors',
        on_delete=models.CASCADE
    )

    icon = models.CharField(
        verbose_name="Иконка",
        default="🍅",
        max_length=core.MAX_LENGTH_NAME_ICON_POMODORS
        )
    
    minute_intensive = models.PositiveIntegerField(
        verbose_name="Время сосредоточения",
    )

    datetime_field = models.DateTimeField(
        default=datetime.now, blank=True,
        verbose_name="Дата и время создание"
    )

    def __str__(self) -> str:
        year = self.datetime_field.date().year
        month = self.datetime_field.date().month
        day = self.datetime_field.date().day
        hour = self.datetime_field.time().hour
        minute = self.datetime_field.time().minute.real
        return f'{self.icon} {self.minute_intensive} минут - {year}.{month}.{day} {hour}:{minute}'
    
    class Meta:
        verbose_name = "Помидор"
        verbose_name_plural = "Помидоры"





class Config(models.Model):
    color = models.CharField(
        verbose_name="Цвет фона",
        default="#9da1aa",
        max_length=core.MAX_LENGTH_COLOR,
    )

    color_navigation = models.CharField(
        verbose_name="Цвет навигации",
        default="#9da1aa",
        max_length=core.MAX_LENGTH_COLOR,
    )
    song_intensive = models.CharField(
        max_length=100,
        verbose_name="URL к мелодии",
        default="/pomodoro/melody/matrix.mp3"
    )

    song_relax = models.CharField(
        max_length=100,
        verbose_name="URL к мелодии",
        default="/pomodoro/melody/matrix.mp3"
    )
    vector = models.CharField(
        max_length=100,
        verbose_name="URL вектора",
        default='none'
    )





class PomodorConfig(models.Model):
    time_intensive = models.PositiveIntegerField(
        verbose_name="Время помидора",
        default=25,
    )
    time_relax = models.PositiveIntegerField(
        verbose_name="Время отдыха",
        default=5,
    )
    theme = models.ForeignKey(
        Theme,
        verbose_name="Выбранная тема",
        related_name='configuration',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
