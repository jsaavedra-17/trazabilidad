import sys
from django.shortcuts import render
from django.http import HttpResponse
from core.static.seekers import busquedaBD_proy

# Create your views here.

def busquedaTrc(request):

    return render(request, "busqueda.html")

def buscado(request):

    #print(request.GET["strUsr"])
    proy_ingresado = request.GET["proy"]
    resultadoProy= busquedaBD_proy(proy_ingresado)




    return render(request, "resultado_busqueda.html", {"proy_buscado": resultadoProy})

