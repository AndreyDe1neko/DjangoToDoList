from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from .models import Customer



menu = {
    "Про сайт": "#", 
    "Мої нотатки": "notes", 
    "Зворотній зв'язок": "#", 
    "Увійти": "auth"
    }

def notes(request):
    # all_cust = Customer.objects.all()
    context = {
        'menu': menu, 
        'title': "Розпорядок дня", 
        # 'all_customers': all_cust,
    }
    return render(request, 'textlist/notes.html', context)

def about(request):
    return render(request, 'textlist/about.html', {'menu': menu, 'title': "О сайте"})

def auth(request):
    return render(request, 'textlist/auth.html', {'menu': menu})

def regist(request):
    return render(request, 'textlist/reg.html', {'menu': menu})


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

