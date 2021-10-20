from django.shortcuts import render
from .models import Items
from django.http import HttpResponse


def home(request):
    items = Items.objects.all()
    return render(request,"formulario.html", {"datos": items})