from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('about', about, name='about'),
    path('', index, name='main'),  #http://127.0.0.1:8000/
    path('refactor_note/<int:refactor_note_id>/', ref_note, name='refactor_note'),
    path('notes/<int:day_of_week>/', notes, name='notes'),
    path('create_note/<int:current_day_of_week>/', create_note, name='create_note'),
    path('delete_note/<int:delete_note_id>/', delete_note, name='delete_note'),

    # path('cats/<int:catid>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]