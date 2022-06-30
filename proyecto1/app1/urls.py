from django.urls import path
from .views import index,creardemanda,listado,modificar_dem

urlpatterns = [
    path('', index, name="home"),
    path('creardemanda/',creardemanda, name="creardemanda"),
    path('list/',listado ,name="list" ),
    path('modificar/<id>/',modificar_dem  ,name="modific"),
  
    
]