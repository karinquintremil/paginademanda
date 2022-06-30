from django.contrib import admin
from app1.models import demanda,tipo_comuna_ante,tipo_comuna_dado,tipo_demanda


# Register your models here.
admin.site.register(demanda)
admin.site.register(tipo_comuna_dado)
admin.site.register(tipo_comuna_ante)
admin.site.register(tipo_demanda)