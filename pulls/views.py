from django.shortcuts import render
from .models import Items
from .forms import frmItem
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ItemSerializers


def home(request):
    items = Items.objects.all()
    formularioItem = frmItem(request.POST or None)
    context = {
        "item": items,
        "formularioItem": formularioItem
        }
    if request.method == "POST":
        data = request.POST
        files = request.FILES
        formularioItem = frmItem(data, files)
        if formularioItem.is_valid():
            formularioItem.save()
            formularioItem.clean()
        return render(request,"formulario.html",context)
    return render(request,"formulario.html",context)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializers


