from datetime import datetime, timezone
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.db.models import QuerySet
from collections import defaultdict
from .forms import CreateTaskForms
from .models import Rest, Theme, Config, Pomodor, PomodorConfig

class PomodoroView(View):
    def get(self, request, *args, **kwargs):
        is_authenticated = request.user.is_authenticated
        if not is_authenticated:
            return redirect('login')
        themes = Theme.objects.filter(author=request.user)
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
            'is_authenticated': is_authenticated,
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
        find_theme = Theme.objects.get(id=theme)

        Pomodor.objects.create(
            theme=find_theme,
            minute_intensive=seconds,
        )

        return HttpResponse(status=201)



class NavigationView(View):
    def get(self, request, *args, **kwargs):
        form = CreateTaskForms()
        themes = Theme.objects.filter(author=request.user)
        config_minutes = PomodorConfig.objects.first().time_intensive
        config_theme = PomodorConfig.objects.first().theme
        color = Config.objects.first().color
        color_navigation = Config.objects.first().color_navigation
        context = {
            'form': form,
            "conf_min": config_minutes,
            "conf_theme": config_theme,
            "themes": themes,
            'color': color,
            'color_navigation': color_navigation,
        }
        return render(request, 'navigation/navigation.html', context)
    
    def post(self, request):
        form = CreateTaskForms(request.POST)
        config = PomodorConfig.objects.first()
        theme_id = request.POST.get('themes')
        minutes = request.POST.get('minutes')
        if form is not None:
            if form.is_valid():
                name = form.cleaned_data['name']
                Theme.objects.create(name=name)
                messages.success(request, 'Данные успешно добавлены.')
                return redirect('dashboard')
        if theme_id:
            theme_id = int(theme_id)
            theme = Theme.objects.get(id=theme_id)
            config.theme = theme
        if minutes:
            config.time_intensive = int(minutes)
        config.save()
        return redirect('dashboard')

    
class TasksView(View):
    def get(self, request, *args, **kwargs):
        themes = Theme.objects.all()

        context = {
            'themes': themes
        }
        return render(request, 'navigation/tasks.html', context)

#Удалить
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
            new_theme = Theme.objects.create(name=name, author=request.user)
            config = PomodorConfig.objects.first()
            config.theme = new_theme
            config.save()
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
        themes = Theme.objects.filter(author=request.user)
        active_theme = PomodorConfig.objects.first().theme.name
        pomodoros_and_rests = {}
        today = datetime.today().replace(tzinfo=timezone.utc)

        formatted_date = today.strftime('%d %B %Y')
        for theme in themes:
            pomodoros_and_rests[theme.name] = theme 

        context = {
            'today': formatted_date,
            'themes': themes,
            'active_theme':active_theme,
            'pomodoros_and_rests': pomodoros_and_rests,
        }
        return render(request, 'stats/stats.html', context)
    

def delete_theme_view(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id)
    theme.delete()
    return redirect('dashboard')

def create_rest(request):
    byte_string = request.body
    json_string = byte_string.decode('utf-8')
    data_dict = json.loads(json_string)
    seconds = data_dict['seconds'] // 60
    theme = data_dict['theme']
    find_theme = Theme.objects.get(id=theme)

    Rest.objects.create(
        theme=find_theme,
        minute_rest=seconds,
    )

    return HttpResponse(status=201)


