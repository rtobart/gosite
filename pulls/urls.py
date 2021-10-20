from django.urls import path
from django.urls import include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('item',ItemViewSet)

urlpatterns = [
    path('', home),
    path('api/', include(router.urls)),
]