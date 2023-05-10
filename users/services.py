from django.http import HttpRequest
from django.contrib import auth

from users.forms import UserLoginForm


def get_user_login_form(request: HttpRequest) -> UserLoginForm:
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
    else:
        form = UserLoginForm()
    return form


def verification_user(request: HttpRequest, form: UserLoginForm) -> None:
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request=request, user=user)

