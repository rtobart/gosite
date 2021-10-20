from django import forms
from django.forms import fields
from pulls.models import *


class frmItem(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('name','price','image')