from django.shortcuts import render
from .models import Items
from .forms import frmItem
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ItemSerializers
from .prediccion import predecir
from django.core.files.storage import default_storage
from django.contrib import messages

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
        # arcImagen = files['image']
        # imagen = arcImagen['InMemoryUploadedFile']            
        file = request.FILES.get('image')
        img = file.open()
        prediccion = predecir(img)
        print(prediccion)
        print(items)
        if formularioItem.is_valid():
            formularioItem.save()
            formularioItem.clean()
        return render(request,"formulario.html",context, message='Save complete')
    return render(request,"formulario.html",context, message='Save complete')

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializers


