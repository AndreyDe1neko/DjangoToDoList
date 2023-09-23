from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from acc.models import User
from .forms import *
from datetime import datetime
from django.contrib.auth import get_user_model

def index(request):
    context = {
    }

    return render(request, 'textlist/index.html', context)


def standart_user_check(func):
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated:

            func(request, *args, **kwargs)
            return JsonResponse({}, status=204)
        else:
            return JsonResponse({'error': 'Not authorized'}, status=401)

    return inner


def notes(request, day_of_week=datetime.isoweekday(datetime.now())):
    if day_of_week <= 7 or day_of_week >= 1:
        days_of_week = [1, 2, 3, 4, 5, 6, 7]
        days_of_week_for_notes = zip(days_of_week, ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "НД"])

        current_user = request.user
        if current_user.is_authenticated:
            all_notes_id = CustNote.objects.filter(cust_note=current_user.id).values_list('note_id', flat=True)
            print(all_notes_id)
            all_notes = Note.objects.filter(id__in=all_notes_id).order_by('time_note')
            context = {
                'title': "Розпорядок дня",
                'all_cust_note': all_notes,
                'week_day': day_of_week,
                'static_week_days': days_of_week_for_notes
            }
            return render(request, 'textlist/notes.html', context)
        else:
            return redirect('login')
    else:
        return JsonResponse({'error': 'Запис не знайдено'}, status=404)


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

# Import get_user_model

def create_note(request, current_day_of_week):
    if current_day_of_week <= 7 or current_day_of_week >= 1:
        try:
            new_note = Note.objects.create(title_note="", time_note="00:00:00", text_note="", telegram_send=False,
                                           day_of_week=current_day_of_week)
            current_user = request.user

            cust_note = Note.objects.get(id=new_note.id)

            User = get_user_model()  # Get the custom User model
            user_curr = User.objects.get(id=current_user.id)
            print(f'{cust_note}  +  {user_curr}')
            data = CustNote(note=cust_note, cust_note=user_curr)
            data.save()
            print(current_user)
            print("--------------", data)
            return JsonResponse(cust_note.pk, safe=False)
        except Note.DoesNotExist:
            return JsonResponse({'error': 'Запис не знайдено'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Запис не знайдено'}, status=400)


def delete_note(request, delete_note_id):
    current_user = request.user
    all_user_notes_id = CustNote.objects.filter(cust_note=current_user.id)
    print(all_user_notes_id)
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
        return HttpResponseNotFound("Попытка удалить не свою запись ")


def ref_note(request, refactor_note_id):
    current_user = request.user
    all_user_notes_id = CustNote.objects.filter(cust_note=current_user.id)
    all_notes_id = [i.note_id for i in all_user_notes_id]
    if refactor_note_id in all_notes_id:
        if request.method == 'POST':
            note_id = request.POST.get('note_id')
            title_text_cur = request.POST.get('title_text_up')
            print(title_text_cur)
            text_note_cur = request.POST.get('text_note_up')
            getTime = request.POST.get('getTime')
            try:
                note = Note.objects.get(id=note_id)
                note.title_note = title_text_cur
                note.text_note = text_note_cur
                note.time_note = getTime
                note.save()
                return JsonResponse({}, status=204)
            except Note.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Note does not exist.'})
        else:
            return JsonResponse({'error': True}, status=204)
    else:
        return JsonResponse({'success': False, 'message': "It's not your note"})

    # else:
    #     return JsonResponse({'error': True}, status=204)

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
