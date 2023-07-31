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


def notes(request):
    all_notes_id = CustNote.objects.filter(cust_note=3)
    all_notes = Note.objects.filter(id__in=all_notes_id).order_by('time_note')

    print(all_notes)

    context = {
        'title': "Розпорядок дня",
        'all_cust_note': all_notes,
    }

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
    context = {

    }
    return render(request, 'textlist/auth.html', context)


def regist(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(form.is_valid())
        print(form.cleaned_data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('notes')
        messages.error(request, "Невдала реєстрація. Перевірте правильність введеної інформації.")
    form = NewUserForm()

    context = {
        'form': form
    }

    return render(request, 'textlist/reg.html', context)


def logout_view(request):
    logout(request)
    return redirect('auth')


@csrf_exempt
def delete_note(request, note_id):
    try:
        note = Note.objects.get(pk=note_id)
        note.delete()
        return JsonResponse({}, status=204)
    except Note.DoesNotExist:
        return JsonResponse({'error': 'Запис не знайдено'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

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
