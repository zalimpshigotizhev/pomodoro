from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from users.views import RegisterUser, LoginUser, LogoutUser

urlpatterns = [
    path('register/', RegisterUser.as_view(), name="register"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', LogoutUser.as_view(), name="logout"),
    path('', include('django.contrib.auth.urls')),
]

