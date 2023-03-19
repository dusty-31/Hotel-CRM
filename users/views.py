from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm


def index_view(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='users/index.html')


@login_required
def user_profile_view(request: HttpRequest) -> HttpResponse:
    user = request.user
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    }
    return render(request=request, template_name='users/profile.html', context=context)


def user_login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request=request, user=user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request=request, template_name='users/login.html', context=context)


def logout_view(request: HttpRequest) -> HttpResponseRedirect:
    auth.logout(request=request)
    return HttpResponseRedirect(reverse('index'))
