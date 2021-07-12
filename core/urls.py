from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name="index"),
    path('main/',views.main ,name="main"),
    path('mecanicos/',views.mecanicos,name="mecanicos"),
    path('trabajos/',views.trabajos,name="trabajos"),
     path('quienessomos/',views.quienessomos ,name="quienessomos"),
 

    ]




