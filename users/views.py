from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from users.services import get_user_login_form, verification_user


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
    form = get_user_login_form(request=request)
    if request.method == "POST":
        verification_user(request=request, form=form)
        return HttpResponseRedirect(reverse('users:profile'))

    context = {
        'title': 'Hotels CRM - Login',
        'form': form,
    }

    return render(request=request, template_name='users/login.html', context=context)


def logout_view(request: HttpRequest) -> HttpResponseRedirect:
    auth.logout(request=request)
    return HttpResponseRedirect(reverse('index'))
