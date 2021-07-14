from django.urls import path
from .views import main,mecanicos,trabajos,quienessomos,agregar_servicio , registro

urlpatterns = [
    path('',main,name="main"),
    path('mecanicos/',mecanicos,name="mecanicos"),
    path('trabajos/',trabajos,name="trabajos"),
    path('quienessomos/',quienessomos ,name="quienessomos"),
    path('agregar_servicio/',agregar_servicio ,name="agregar_servicio"),
    path('registro/',registro,name="registro"),

   

]




