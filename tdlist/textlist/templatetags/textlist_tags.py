from django import template
from textlist.models import *

register = template.Library()

@register.simple_tag(name='getnote') # Сделать из функции простой тег (для того, чтобы использовать его в коде и не повторять код)
def get_note_all():
    return Note.objects.all()

@register.inclusion_tag('textlist/note_days.html')
def show_notes_by_days():
    notes = Note.objects.all()
    return {"notes": notes}