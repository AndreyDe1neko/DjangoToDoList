from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('notes', notes, name='notes'), #http://127.0.0.1:8000/
    path('about', about, name='about'),
    path('auth', auth, name="auth"),
    path('reg', regist, name="reg")
    # path('cats/<int:catid>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]