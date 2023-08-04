from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


def index(request):
    context = {
    }

    return render(request, 'textlist/index.html', context)


def notes(request, day_of_week=datetime.isoweekday(datetime.now())):
    if request.user.is_authenticated:
        current_user = request.user
        all_notes_id = CustNote.objects.filter(cust_note=current_user.id)
        all_notes = Note.objects.filter(id__in=all_notes_id).order_by('time_note')

        context = {
            'title': "Розпорядок дня",
            'all_cust_note': all_notes,
            'week_day': day_of_week
        }
    else:
        return redirect('auth')
    return render(request, 'textlist/notes.html', context)


# def show_note(request, note_slug):
#     # note = get_object_or_404(Note, slug=note_slug)

#     context = {
#         # 'note': note,
#         'menu': menu, 
#         'title': "О сайте"
#     }
#     return render(request, 'textlist/show_note.html', context)

def about(request):
    context = {
        'title': "О сайте"
    }
    return render(request, 'textlist/about.html', context)


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
            return redirect('notes/1/')
        messages.error(request, "Невдала реєстрація. Перевірте правильність введеної інформації.")
    form = NewUserForm()

    context = {
        'form': form
    }

    return render(request, 'textlist/reg.html', context)


def logout_view(request):
    logout(request)
    return redirect('auth')

# @requaire_POST

def create_note(request):
     pass


def delete_note(request, delete_note_id):

    current_user = request.user
    all_user_notes_id = CustNote.objects.filter(cust_note=current_user.id)
    all_notes_id = [i.note_id for i in all_user_notes_id]
    if delete_note_id in all_notes_id:
        try:
            note = Note.objects.get(pk=delete_note_id)
            note.delete()
            return JsonResponse({}, status=204)
        except Note.DoesNotExist:
            return JsonResponse({'error': 'Запис не знайдено'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        print("suck dick")

# def categories(request, catid):
#     if request.GET:
#         print(request.GET) 
#     return HttpResponse(f"<h1>Your number is {catid}</h1>")

# def archive(request, year):
#     if int(year) > 2023:
#         raise Http404()
#     elif int(year) < 1990:
#         return redirect('home', permanent=True)
#     return HttpResponse(f"<h1>re_path test {year}</h1>")

# def pageNotFound(request, exception):
#     return HttpResponseNotFound("<h1>Страница не найдена</h1>")
