from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Items

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['id','name','price','image']