from django.db import models
from django.urls import reverse


# Create your models here.

class Customer(models.Model):
    name_cust = models.CharField(max_length=255, verbose_name = "Ім'я", unique=True)
    mail_cust = models.TextField(blank=True, verbose_name = "Пошта користувача", unique=True)
    phone_cust = models.TextField(max_length=15, blank=True, verbose_name = "Телефон")
    password_cust = models.TextField(max_length=255, verbose_name = "Пароль")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = "Дата та час створення акаунту")   # Добавление текущего времени без изменений
    time_update = models.DateTimeField(auto_now=True, verbose_name = "Последнее редактирование")       # Добавление текущего времени с изменением
    
    def __str__(self):
        return self.name_cust
    
    # def all_customers(self):
    #     return self.objects.get()
    
    # def get_customer_(self):
    #     return self.objects.all()
    
    class Meta:
        verbose_name="Пользователи"
        verbose_name_plural = "Пользователи"
        ordering = ["name_cust", "time_create"]
    
    # def get_absolute_url(self):                             # Метод для вынимаия данных, в html коде потом прописать "NAME_peremennaya.get_absolute_url"
    #     return reverse('post', kwargs={'Customer_id': self.pk})

class Note(models.Model):
    title_note = models.TextField(max_length=255, blank=True)
    time_note = models.TimeField()
    text_note = models.TextField(max_length=1000, blank=True)
    telegram_send = models.BooleanField(default=False)
    day_of_week = models.SmallIntegerField()
    
    def __str__(self):
        return self.title_note
    
    def get_absolute_url(self):                             # Метод для вынимаия данных, в html коде потом прописать "NAME_peremennaya.get_absolute_url"
        return reverse('note', kwargs={'note_slug': self.slug})
    
    class Meta:
        verbose_name="Нотатка"
        verbose_name_plural = "Нотатки"
        ordering = ["title_note", "time_note"]

    
    
class CustNote(models.Model):
    note = models.ForeignKey('Note', on_delete=models.PROTECT, unique=True)
    cust_note = models.ForeignKey('Customer', on_delete=models.PROTECT)

    
    
