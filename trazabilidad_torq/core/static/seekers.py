from django.shortcuts import render
from django.http import HttpResponse
from core.models import Tuercas

#buscador de tuercas en BD por criterios

'''Busqueda de objetos por proyecto'''
def busquedaBD_proy(proy_ingresado):

    resultadoProy = Tuercas.objects.filter(proyecto=proy_ingresado)

    if resultadoProy.exists():
        print("busqueda con coincidencias")

    else:
        print("busqueda SIN coincidencias")

    return resultadoProy


