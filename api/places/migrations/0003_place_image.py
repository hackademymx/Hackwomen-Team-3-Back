# Generated by Django 4.0.3 on 2023-04-21 01:02

from django.db import migrations, models
import places.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_rename_adress_city_place_address_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=places.models.upload_load),
        ),
    ]