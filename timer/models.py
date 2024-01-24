from datetime import datetime, timezone
from django.conf import settings
from django.db import models
import core

class Theme(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        verbose_name='Название темы',
        max_length=core.MAX_LENGTH_NAME_THEME
    )
    def __str__(self) -> str:
        return self.name
    
    @staticmethod
    def formating_minutes_in_str(minutes):
        hours = minutes // 60
        minute = minutes % 60
        if hours:
            return f'{hours}.{minute} час'
        return f'{minute} минут'

    
    def get_pomodors_count(self):
        return self.pomodors.count()
    
    def get_pomodoros_today(self):
        today = datetime.now(timezone.utc)
        return self.pomodors.all().filter(datetime_field__date=today.date())
    
    def get_rests_today(self):
        today = datetime.now(timezone.utc)
        return self.rest.all().filter(datetime_field__date=today.date())
    
    def get_pomdoros_rest_today(self):
        pomodoros_today = self.get_pomodoros_today()
        rests_today = self.get_rests_today()
        data = pomodoros_today.union(rests_today)
        sorted_data = data.order_by('datetime_field')
        return sorted_data
    

    def get_time_pomodoros(self):
        pomodoros = self.get_pomodoros_today()
        minutes = 0
        for pomodor in pomodoros:
            minutes += pomodor.minute_intensive
        return self.formating_minutes_in_str(minutes)
    
    def get_time_rests(self):
        rests = self.get_rests_today()
        minutes = 0
        for rest in rests:
            minutes += rest.minute_rest
        return self.formating_minutes_in_str(minutes)
    
    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"        



class Rest(models.Model):
    theme = models.ForeignKey(
        Theme,
        related_name='rest',
        on_delete=models.CASCADE
    )

    icon = models.CharField(
        verbose_name="Иконка",
        default="🏖️",
        max_length=10
    )

    minute_rest = models.PositiveIntegerField(
        verbose_name="Время сосредоточения",
    )

    datetime_field = models.DateTimeField(
        default=datetime.now, blank=True,
        verbose_name="Дата и время создание"
    )

    def __str__(self) -> str:
        date = self.datetime_field.date()
        time = self.datetime_field.strftime('%H:%M')
        return f'{self.icon} {self.minute_rest} минут - {date} {time}'
    
    class Meta:
        verbose_name = "Отдых"
        verbose_name_plural = "Отдыхи"


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
        date = self.datetime_field.strftime('%d/%m/%y')
        time = self.datetime_field.strftime('%H:%M')
        return f'{self.icon} {self.minute_intensive} минут - {date} {time}'
    
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

class Rest(models.Model):
    theme = models.ForeignKey(
        Theme,
        related_name='rest',
        on_delete=models.CASCADE
    )

    icon = models.CharField(
        verbose_name="Иконка",
        default="🏖️",
        max_length=10
    )

    minute_rest = models.PositiveIntegerField(
        verbose_name="Время сосредоточения",
    )

    datetime_field = models.DateTimeField(
        default=datetime.now, blank=True,
        verbose_name="Дата и время создание"
    )

    def __str__(self) -> str:
        date = self.datetime_field.date()
        time = self.datetime_field.strftime('%H:%M')
        return f'{self.icon} {self.minute_rest} минут - {date} {time}'
    
    class Meta:
        verbose_name = "Отдых"
        verbose_name_plural = "Отдыхи"


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
        date = self.datetime_field.strftime('%d/%m/%y')
        time = self.datetime_field.strftime('%H:%M')
        return f'{self.icon} {self.minute_intensive} минут - {date} {time}'
    
    class Meta:
        verbose_name = "Помидор"
        verbose_name_plural = "Помидоры"





# class Profile(models.Model):
#     # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь", null=True, blank=True)

#     color = models.CharField(
#         verbose_name="Цвет фона",
#         default="#9da1aa",
#         max_length=core.MAX_LENGTH_COLOR,
#     )

#     time_intensive = models.PositiveIntegerField(
#         verbose_name="Время помидора",
#         default=25,
#     )

#     time_relax = models.PositiveIntegerField(
#         verbose_name="Время отдыха",
#         default=5,
#     )

#     theme = models.ForeignKey(
#         Theme,
#         verbose_name="Выбранная тема",
#         related_name='configuration',
#         on_delete=models.SET_NULL,
#         blank=True,
#         null=True
#     )

#     song_intensive = models.CharField(
#         max_length=100,
#         verbose_name="URL к мелодии",
#         default="/pomodoro/melody/matrix.mp3"
#     )

#     song_relax = models.CharField(
#         max_length=100,
#         verbose_name="URL к мелодии",
#         default="/pomodoro/melody/matrix.mp3"
#     )
    
#     vector = models.CharField(
#         max_length=100,
#         verbose_name="URL вектора",
#         default='none'
#     )
#     def __str__(self):
#         return self.user.username