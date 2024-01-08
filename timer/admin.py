from django.contrib import admin
from .models import PomodorConfig, Theme, Pomodor, Config


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    pass

@admin.register(PomodorConfig)
class PomodoroConfigAdmin(admin.ModelAdmin):
    pass



@admin.register(Pomodor)
class PomodorAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        # Добавьте поля, которые вы хотите отобразить в списке объектов
        return  super().get_list_display(request) + ('theme',)