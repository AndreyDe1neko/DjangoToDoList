# Generated by Django 4.2.3 on 2023-07-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textlist', '0004_alter_customer_photo_cust'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='photo_cust',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
