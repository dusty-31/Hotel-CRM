from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from .forms import UserLoginForm


def index_view(request):
    return render(request=request, template_name='users/index.html')


def user_profile_view(request):
    return render(request=request, template_name='users/profile.html')


def user_login_view(request):
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
