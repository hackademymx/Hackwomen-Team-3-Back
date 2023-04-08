from django.db import models

def upload_load(instance, filename):
    return f'photos_places/{instance.name}/{filename}'

# Create your models here.


class Place(models.Model):

    name = models.CharField(max_length=56)
    description = models.CharField(max_length=256)
    address_state =models.CharField(max_length=32)
    adress_city= models.CharField(max_length=32)
    address_colonia =models.CharField(max_length=32)
    address_street= models.CharField(max_length=32)
    adress_zipcode= models.CharField(max_length=32)
    #image = models.ImageField(upload_to=upload_load, default='default.jpg', null=False)

    class Meta:
        db_table= 'places'
    
    def __str__(self):
        return self.name