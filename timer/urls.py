from django.contrib import admin
from django.urls import include, path
from timer.views import AppereanceView, ConfigView, PomodoroView, NavigationView, StatsView, TasksView, CreateTasksView, delete_theme_view, create_rest

urlpatterns = [
    path('', PomodoroView.as_view(), name='dashboard'),
    path('navigation/', NavigationView.as_view(), name='navigation'),
    path('tasks/', TasksView.as_view(), name='tasks'),
    path('create_tasks/', CreateTasksView.as_view(), name='create_tasks'),
    path('config/', ConfigView.as_view(), name='config'),
    path('appearance/', AppereanceView.as_view(), name='appearance'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('delete_theme/<int:theme_id>/', delete_theme_view, name='delete_theme'),
    path('create_rest/', create_rest, name='create_rest'),
]