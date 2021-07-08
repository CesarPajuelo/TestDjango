from django.urls import path
from .views import index,mecanicos

urlpatterns = [
    path('',index,name="index"),
    path('mecanicos/',mecanicos,name="mecanicos"),

    ]




