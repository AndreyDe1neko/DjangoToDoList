from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    title_note = models.TextField(max_length=255, blank=True)
    time_note = models.TimeField()
    text_note = models.TextField(max_length=1000, blank=True)
    telegram_send = models.BooleanField(default=False)
    day_of_week = models.SmallIntegerField()

    def __str__(self):
        return self.title_note

    # def get_absolute_url(self):                             # Метод для вынимаия данных, в html коде потом прописать "NAME_peremennaya.get_absolute_url"
    #     return reverse('note', kwargs={'note_slug': self.slug})

    class Meta:
        verbose_name = "Нотатка"
        verbose_name_plural = "Нотатки"
        ordering = ["title_note", "time_note"]

class CustNote(models.Model):
    note = models.ForeignKey('Note', on_delete=models.PROTECT, unique=True)
    cust_note = models.ForeignKey(User, on_delete=models.PROTECT)



