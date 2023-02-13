from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User
from django.views.generic import (CreateView, UpdateView, TemplateView)
from django.contrib.auth.views import LoginView, LogoutView
from .models import Profile
# Create your views here.

class SuccessUrlMixin:
    """Success mixin class"""

    def get_success_url(self):
        return reverse("users:profile", kwargs = {'user_name': self.request.user.username})

class RegisterView(CreateView):
    """Register class"""

    model = User
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

class LoginView(SuccessUrlMixin, LoginView):
    """Login class"""

    template_name = "users/login.html"

def profile(request,user_name):
    """Profile function"""

    if user_name != request.user.username:
        return redirect('movie:index')
    user = User.objects.get(username=request.user.username)
    return render(request, 'users/profile.html', {'user': user})

class UpdateUserView(SuccessUrlMixin,UpdateView):
    """Update user class"""

    template_name = 'users/update.html'
    context_object_name = 'user'
    model = Profile
    form_class = ProfileUpdateForm

    def get_context_data(self, **kwargs):
        """Get context data function"""

        if kwargs['user_name'] != self.request.user.username:
            return redirect('movie:index')
        context = super(UpdateUserView, self).get_context_data(**kwargs)
        context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context

class Logout(LogoutView):
    """Log out class"""
    
    next_page = "movie:index"