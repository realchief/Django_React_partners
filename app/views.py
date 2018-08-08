import requests
from requests.auth import HTTPBasicAuth

from django.conf import settings
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .decorators import render_to


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')


@render_to('home.html')
def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated:
        return redirect('done')


@login_required
@render_to('home.html')
def done(request):
    resp = requests.request('get', settings.SM_USER_TOKEN_URL.format(request.user.email),
                            auth=HTTPBasicAuth(settings.SM_USER, settings.SM_PASSWORD))
    if resp.status_code == 200:
        token = resp.json()['key']
        redirect(settings.SM_LOGIN_URL.format(token))

    """Login complete view, displays user data"""
    pass
