from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, AccountAuthenticationForm
from .urls import *


def registration_view(request):
    context = {}
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('accounts:signin')
        else:
            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def authentication(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('general:home_page')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('general:home_page')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/signin.html', context)


def signout_view(request):
    logout(request)
    return redirect('accounts:starting')


def starting(request):
    context = {}
    return render(request, 'account/start.html')
