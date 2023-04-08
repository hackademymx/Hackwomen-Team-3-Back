# Generated by Django 4.0.3 on 2023-04-08 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('description', models.CharField(max_length=256)),
                ('address_state', models.CharField(max_length=32)),
                ('adress_city', models.CharField(max_length=32)),
                ('address_colonia', models.CharField(max_length=32)),
                ('address_street', models.CharField(max_length=32)),
                ('adress_zipcode', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'places',
            },
        ),
    ]
