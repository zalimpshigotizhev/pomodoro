from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegisterUserForm, LoginUserForm
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView

# class LoginUser(DataMixin, LoginView):
class RegisterUser(View):

    def get(self, request, *args, **kwargs):
        form_class = RegisterUserForm
        context = {
            'form': form_class
        }
        return render(request, 'registration/register.html', context)
    
    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')  # Replace 'login' with the actual URL name for your login page
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
            context = {
                'form': form
            }
            return render(request, 'auth/register.html', context)
    
class LoginUser(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = 'dashboard'
    form_class = LoginUserForm
    
    def get_success_url(self):
        return reverse_lazy('dashboard')

class LogoutUser(LogoutView):
    next_page = 'dashboard'
    
    
    