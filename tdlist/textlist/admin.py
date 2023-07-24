from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name_cust", "mail_cust", "time_create", "time_update")
    list_display_links = ("id", "name_cust", "mail_cust")
    search_fields = ("name_cust", "mail_cust", "phone_cust")

class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "title_note", "time_note", "text_note", "telegram_send", "day_of_week")
    list_display_links = ("id", "title_note", "text_note")
    search_fields = ("title_note", "text_note")

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Note, NoteAdmin)
