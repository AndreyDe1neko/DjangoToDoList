from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


menu = {
    "Про сайт": "#", 
    "Мої нотатки": "notes", 
    "Зворотній зв'язок": "#", 
    "Увійти": "auth"
    }

def notes(request):
    all_notes_id = CustNote.objects.filter(cust_note=3)
    all_notes = Note.objects.filter(id__in=all_notes_id).order_by('time_note')
    
    print(all_notes)

    context = {
        'menu': menu, 
        'title': "Розпорядок дня", 
        'all_cust_note': all_notes,
        
    }
    return render(request, 'textlist/notes.html', context)

def about(request):
    return render(request, 'textlist/about.html', {'menu': menu, 'title': "О сайте"})

def auth(request):
    return render(request, 'textlist/auth.html', {'menu': menu})

def regist(request):
    return render(request, 'textlist/reg.html', {'menu': menu})

@csrf_exempt
def delete_note(request, note_id):
    # Виконайте логіку для видалення запису з бази даних за допомогою Django ORM
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

