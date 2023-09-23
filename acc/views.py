import threading

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str

from textlist.forms import LoginForm
from .utils import generate_token
from .forms import *
from datetime import datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings
from django.db import IntegrityError

class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_action_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate you acc'
    email_body = render_to_string('Authentication/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
        })
    email = EmailMessage(subject=email_subject,
                 body=email_body,
                 from_email=settings.EMAIL_FROM_USER,
                 to=[user.email]
                 )

    EmailThread(email).start()


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

        # messages.add_message(request, messages.SUCCESS, f'Well cum {user.email}')
    return render(request, 'Authentication/auth.html', context)


def regist(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            # Check if the username is unique
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken. Please choose a different one.')
            # Check if the email is unique
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email address is already registered. Please use a different email.')
            else:
                # Create the user if both username and email are unique
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password1)
                user.save()
                send_action_email(user, request)
                messages.success(request, 'Account created successfully. You can now log in.')
                return redirect('login')
        else:
            # Form validation failed, display errors
            messages.error(request, 'Registration failed. Please check the provided information.')

    else:
        form = NewUserForm()

    context = {
        'form': form
    }

    return render(request, 'Authentication/reg.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        print(uid)
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified=True
        user.save()

        messages.add_message(request, messages.SUCCESS, 'Email verified')
        return redirect('login')

    return render(request, 'authentication/activate-failed.html', {'user': user})


class WebPasswordResetView(PasswordResetView):
    template_name = 'authentication/password_reset_email.html'


class WebPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html'


class WebPasswordResetConfirmationView(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirmation.html'
