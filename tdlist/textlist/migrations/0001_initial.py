# Generated by Django 4.2.3 on 2023-07-15 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cust', models.CharField(max_length=255)),
                ('mail_cust', models.TextField(blank=True)),
                ('phone_cust', models.TextField(blank=True, max_length=15)),
                ('password_cust', models.TextField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_note', models.TextField(blank=True, max_length=255)),
                ('time_note', models.TimeField()),
                ('text_note', models.TextField(blank=True, max_length=1000)),
                ('telegram_send', models.BooleanField(default=False)),
                ('day_of_week', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CustNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_note', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='textlist.customer')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='textlist.note')),
            ],
        ),
    ]