"""pomodoro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from timer.views import AppereanceView, ConfigView, PomodoroView, NavigationView, StatsView, TasksView, CreateTasksView, delete_theme_view, get_csrf_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', PomodoroView.as_view(), name='dashboard'),
    path('navigation/', NavigationView.as_view(), name='navigation'),
    path('tasks/', TasksView.as_view(), name='tasks'),
    path('create_tasks/', CreateTasksView.as_view(), name='create_tasks'),
    path('config/', ConfigView.as_view(), name='config'),
    path('appearance/', AppereanceView.as_view(), name='appearance'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('delete_theme/<int:theme_id>/', delete_theme_view, name='delete_theme'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf')


]
