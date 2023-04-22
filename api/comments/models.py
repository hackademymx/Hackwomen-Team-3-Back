from django.db import models
from places.models import Place

# Create your models here.


class Comment(models.Model):

    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table= 'comments'
    
    def __str__(self):
        return self.comment