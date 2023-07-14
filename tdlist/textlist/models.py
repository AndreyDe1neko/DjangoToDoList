from django.db import models
from django.urls import reverse

# Create your models here.

class Customer(models.Model):
    name_cust = models.CharField(max_length=255)
    mail_cust = models.TextField(blank=True)
    phone_cust = models.TextField(max_length=15, blank=True)
    password_cust = models.TextField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)   # Добавление текущего времени без изменений
    time_update = models.DateTimeField(auto_now=True)       # Добавление текущего времени с изменением
    
    def __str__(self):
        return self.name_cust
    
    def get_absolute_url(self):                             # Метод для вынимаия данных, в html коде потом прописать "NAME_peremennaya.get_absolute_url"
        return reverse('post', kwargs={'Customer_id': self.pk})

class Note(models.Model):
    title_note = models.TextField(max_length=255, blank=True)
    time_note = models.DateField()
    text_note = models.TextField(max_length=1000, blank=True)
    telegram_send = models.BooleanField(default=False)

    
class CustNote(models.Model):
    note = models.ForeignKey('Note', on_delete=models.PROTECT)
    cust_note = models.ForeignKey('Customer', on_delete=models.PROTECT)
    
    
    
