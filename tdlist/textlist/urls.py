from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('notes/<int:day_of_week>/', notes, name='notes'),
    path('about', about, name='about'),
    path('auth', auth, name="auth"),
    path('reg', regist, name="reg"),
    path('', index, name='main'),  #http://127.0.0.1:8000/
    path('logout', logout_view, name='logout'),
    path('create_note/', create_note, name='create_note'),
    path('delete_note/<int:note_id>/', delete_note, name='delete_note'),
    # path('cats/<int:catid>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]