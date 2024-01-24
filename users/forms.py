from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', max_length=70, required=True, widget=forms.TextInput())
    username = forms.CharField(label='Логин',widget=forms.TextInput() )
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput())
    password1 = forms.CharField(label='Пароль', required=True, widget= forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', required=True, widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput())
    password = forms.CharField(label='Пароль', required=True, widget= forms.PasswordInput())

    class Meta:
        model = User