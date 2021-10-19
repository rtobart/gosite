from django.db import models

# Create your models here.
class Items(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField
    image = models.ImageField(upload_to='items',null=True)