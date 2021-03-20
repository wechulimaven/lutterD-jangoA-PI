from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from Oaurth.forms import *
from Oaurth.models import *

import requests


def user_login(request):

    template_name = 'Ouarth/signin.html'
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':

        form = UserLoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            login(request, user)

            # AuthTokenApi
            # authenticate with FB Function API

            API_URL = "https://us-central1-ecommerce-47123.cloudfunctions.net/maberr_admin_api/v1/admin_oauth/adminAuthentication/"

            user_auth_data = {
                "email": f"{username}@g.net",
                "password": password,
                "returnSecureToken": True
            }

            response = requests.post(API_URL, json=user_auth_data)

            resdata = response.json()
            try:
                if (response.status_code == 200 and resdata['idToken'] != ''):
                    # error

                    # kind = resdata['kind']
                    # localId = resdata['localId']
                    # email = resdata['email']
                    # idToken = resdata['idToken']

                    # registered = resdata['registered']
                    # refreshToken = resdata['refreshToken']
                    # expiresIn = resdata['expiresIn']

                    # print(resdata)
                    # print(email)
                    # print(idToken)


                    try:
                        obj, created = AuthTokenApi.objects.update_or_create(
                            kind=resdata['kind'],
                            localId=resdata['localId'],
                            email=resdata['email'],
                            idToken=resdata['idToken'],
                            user=request.user,
                            registered=resdata['registered'],
                            refreshToken=resdata['refreshToken'],
                            expiresIn=resdata['expiresIn'],
                            defaults={},
                        )
                    except IntegrityError:

                        AuthTokenApi.objects.filter(user_id=request.user.id).update(
                            kind=resdata['kind'],
                            localId=resdata['localId'],
                            email=resdata['email'],
                            idToken=resdata['idToken'],
                            registered=resdata['registered'],
                            refreshToken=resdata['refreshToken'],
                            expiresIn=resdata['expiresIn'],
                        )

                    # obj.save()

                    messages.success(request, f'login was successful')

                    return redirect('dashboard')

                else:
                    messages.success(request, f'User Not Found')
                    redirect('logout')
            except KeyError:
                messages.success(request, f'User Not Found')
                redirect('logout')

        else:
            messages.warning(
                request, f'login Error !!!! Provide Correct Username And Password')
            return redirect('login')
    else:
        form = UserLoginForm()

    return render(request, template_name, {'form': form})


def register(request):
    template_name = 'Ouarth/signup.html'

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! Now Login')
            form.save()
            return redirect('login')  # will change to dashboard
        else:
            return redirect('register')
    else:
        form = UserRegisterForm()

    return render(request, template_name, {'form': form})


@staff_member_required(login_url='register')
def user_dashboard(request):

    template_name = 'pages/index.html'

    return render(request, template_name)


def user_loguot(request):
    logout(request)
    messages.success(request, f'You Have logout !!!')
    return redirect('login')
