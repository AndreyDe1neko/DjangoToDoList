from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse

from .models import *
from .forms import *
from datetime import datetime
from textlist.models import User
from django.views.decorators.csrf import csrf_exempt


def auth(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(f'notes/{datetime.isoweekday(datetime.now())}')
            else:
                messages.error(request, "Неправильне ім'я користувача або пароль.")
        else:
            messages.error(request, "Неправильне ім'я користувача або пароль.")
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'textlist/auth.html', context)


def regist(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            url = reverse('notes', kwargs={'day_of_week': 1})
            return redirect(url)
        messages.error(request, "Невдала реєстрація. Перевірте правильність введеної інформації.")
    form = NewUserForm()

    context = {
        'form': form
    }

    return render(request, 'textlist/reg.html', context)


def logout_view(request):
    logout(request)
    return redirect('auth')