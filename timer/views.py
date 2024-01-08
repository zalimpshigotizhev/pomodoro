from datetime import datetime, timezone
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.core.serializers.json import DjangoJSONEncoder
import json

from .forms import UploadFileForm, CreateTaskForms
from .models import Theme, Config, Pomodor, PomodorConfig

class PomodoroView(View):
    def get(self, request, *args, **kwargs):
        themes = Theme.objects.all()
        appereance_conf = Config.objects.first()

        config_minutes = PomodorConfig.objects.first().time_intensive
        config_theme = PomodorConfig.objects.first().theme
        color = appereance_conf.color
        color_navigation = appereance_conf.color_navigation
        themes_data = [{'name': theme.name, 'count': theme.get_pomodors_count()} for theme in themes]
        themes_data = json.dumps(themes_data, cls=DjangoJSONEncoder)
        song_relax = appereance_conf.song_relax
        song_intensive = appereance_conf.song_intensive
        vector = appereance_conf.vector


        context = {
            "conf_min": config_minutes,
            "conf_theme": config_theme,
            'themes': themes,
            'themes_json': themes_data,
            'color': color,
            'color_navigation': color_navigation,
            "song_relax": song_relax,
            "song_intensive": song_intensive,
            "vector": vector
        }
        return render(request, 'pomodoros.html', context)
    
    def post(self, request, *args, **kwargs):
        byte_string = request.body
        json_string = byte_string.decode('utf-8')
        data_dict = json.loads(json_string)
        seconds = data_dict['seconds'] // 60
        theme = data_dict['theme']

        Pomodor.objects.create(
            theme=Theme.objects.get(id=theme),
            minute_intensive=seconds,
        )
        return HttpResponse(status=201)

class NavigationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'navigation/navigation.html')
    
class TasksView(View):
    def get(self, request, *args, **kwargs):
        themes = Theme.objects.all()

        context = {
            'themes': themes
        }
        return render(request, 'navigation/tasks.html', context)
    
class CreateTasksView(View):
    def get(self, request, *args, **kwargs):
        form = CreateTaskForms()

        context = {
            'form': form
        }
        return render(request, 'navigation/create_tasks.html', context)
    
    def post(self, request):
        form = CreateTaskForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Theme.objects.create(name=name)
            messages.success(request, 'Данные успешно добавлены.')
            return redirect('dashboard')


class ConfigView(View):
    def get(self, request, *args, **kwargs):
        themes = Theme.objects.all()
        config_minutes = PomodorConfig.objects.first().time_intensive
        config_theme = PomodorConfig.objects.first().theme



        context = {
            "conf_min": config_minutes,
            "conf_theme": config_theme,
            "themes": themes,
        }
        return render(request, 'navigation/config.html', context)
    
    def post(self, request):
        config = PomodorConfig.objects.first()
        theme_id = request.POST.get('themes')
        minutes = request.POST.get('minutes')

        if theme_id:
            theme_id = int(theme_id)
            theme = Theme.objects.get(id=theme_id)
            config.theme = theme
        if minutes:
            config.time_intensive = int(minutes)
        config.save()
        return redirect('dashboard')

class AppereanceView(View):
    def get(self, request, *args, **kwargs):
        color = Config.objects.first().color
        color_navigation = Config.objects.first().color_navigation

        context = {
            'color': color,
            'color_navigation': color_navigation
        }
        return render(request, 'navigation/appearance.html', context)
    
    def post(self, request):
        config_instance = Config.objects.first()

        color = request.POST.get('color', '')  # 'head' - это имя вашего input элемента
        color_navigation = request.POST.get('color_navigation', '')
        song_relax = request.POST.get('relax')
        song_work = request.POST.get('work')
        vector = request.POST.get('vector')

        if vector:
            config_instance.vector = vector

        if song_relax:
            config_instance.song_relax = song_relax
            
        if song_work:
            config_instance.song_intensive = song_work

        if color:
            config_instance.color = color

        if color_navigation:
            config_instance.color_navigation = color_navigation

        config_instance.save()

        return redirect('dashboard')

class StatsView(View):
    def get(self, request, *args, **kwargs):
        themes = Theme.objects.all()
        today = datetime.now(timezone.utc)
        pomodor_today = Pomodor.objects.filter(datetime_field__date=today.date())
        context = {
            'themes': themes,
            'pomodor_today':pomodor_today[::-1]

        }
        return render(request, 'stats/stats.html', context)
    

def delete_theme_view(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id)
    theme.delete()
    return redirect('dashboard')

from django.views.decorators.csrf import get_token

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})