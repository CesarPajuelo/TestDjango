from django import forms
from.models import Trabajo
from django.contrib.auth.forms import UserCreationForm 



class TrabajoForm(forms.ModelForm):

    class Meta:
        model = Trabajo
        fields = '__all__'

        widgets = {
            "fecha_problema": forms.SelectDateWidget()       
            
        }

class CustomUserCreationForm(UserCreationForm):
    pass