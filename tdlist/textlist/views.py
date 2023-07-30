from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
from .forms import *
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


menu = {
    "Про сайт": "#", 
    "Мої нотатки": "notes", 
    "Зворотній зв'язок": "#", 
    "Увійти": "auth"
    }

def index(request):
    
    context = {
        'menu': menu
    }
    
    return render(request, 'textlist/index.html', context)

def get(request):
    if request.user.is_authenticated:
        customers = Customer.objects.all()
        ctx = {}
        ctx['customers'] = customers
        return render(request, "", ctx)
    else:
        return render(request, "", {})
        
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
        'menu': menu, 
        'title': "О сайте"
    }
    return render(request, 'textlist/about.html', context)

def auth(request):
    return render(request, 'textlist/auth.html', {'menu': menu})

def regist(request):
    error = 'Иди нахуй'
    if request.method == 'POST':
        form = AddCustomer(request.POST)
        if form.is_valid():
            form.save()
        else:
            error='Иди нахуй'
        
    form = AddCustomer()
    context = {
        'menu':menu,
        'form':form,
        'error': error
    }
    
    return render(request, 'textlist/reg.html', context)

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

