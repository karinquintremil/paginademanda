from re import TEMPLATE
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest,HttpResponse
from .models import demanda
from .forms import DemandaForm



# Create your views here.
# TEMPLATE_DIRS=(
#     'os.path.join(BASE.DIR, "templates")'
# )

def index(request):
    return render(request, "index.html")


def creardemanda(request):
    data={
        'form':DemandaForm()
    }

    if request.method=='POST':
        formulario= DemandaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="demanda guardado correctamente"
            data['form']=formulario
        data['form']=formulario
        
    return render (request,'/templates/creardemanda.html',data)



def listado(request):
    listar = demanda.objects.all()
    data = {
        'listar':listar
    }
    return render(request,'/templates/list.html',data)



def modificar_dem(request,id ):
    dem=demanda.objects.get(id= id)
    data = {
        'form':DemandaForm(instance= dem)
    }
    if request.method == 'POST':
        formulario= DemandaForm(data=request.POST, instance=dem )
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "demanda modificada"
            data['form']= formulario
        data['form'] = formulario
    return render(request,'./templates/modificar.html',data)
