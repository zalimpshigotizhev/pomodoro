from django.contrib import admin
from .models import Rest, Theme, Pomodor


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass



@admin.register(Pomodor)
class PomodorAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        # Добавьте поля, которые вы хотите отобразить в списке объектов
        return  super().get_list_display(request) + ('theme',)

@admin.register(Rest)
class RestAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        # Добавьте поля, которые вы хотите отобразить в списке объектов
        return  super().get_list_display(request) + ('theme',)


class PomodorInline(admin.TabularInline):  # Вы также можете использовать admin.StackedInline для другого стиля отображения
    model = Pomodor
