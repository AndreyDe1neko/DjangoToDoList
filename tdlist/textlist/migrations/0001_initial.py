# Generated by Django 4.2.3 on 2023-09-17 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
            options={
                'verbose_name': 'Нотатка',
                'verbose_name_plural': 'Нотатки',
                'ordering': ['title_note', 'time_note'],
            },
        ),
        migrations.CreateModel(
            name='CustNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_note', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('note', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='textlist.note')),
            ],
        ),
    ]
