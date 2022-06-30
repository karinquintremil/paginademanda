from socket import timeout
from time import time
from django import forms
from django.forms import ModelForm
from .models import demanda

class DemandaForm(ModelForm):
    class Meta:
        model= demanda
        fields=['fecha','hora','tpo_dem','detalle','rut_dado','nombre_dado','apellido_dado','telefono_dado','comuna_dado','rut_dante','nombre_dante','apellido_dante','telefono_dante','comuna_dante']
        widgets = {
            'fecha':forms.SelectDateWidget(years=range(2022,2222))
            # 'hora':forms.SelectDateWidget(timeout=range(0000,2400))
        }
        # widgets ={
        #     'hora': DateTimeInput(format=' %H:%M', attrs={'type': 'datetime'},)
        # }


