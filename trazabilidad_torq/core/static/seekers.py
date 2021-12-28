from django.shortcuts import render
from django.http import HttpResponse
from core.models import Union

#buscador de tuercas en BD por criterios

'''Busqueda de objetos por proyecto'''
def busquedaBD_proy(proy_ingresado):

    resultadoProy = Union.objects.filter(id_perno=proy_ingresado)

    if resultadoProy.exists():
        print("busqueda con coincidencias")

    else:
        print("busqueda SIN coincidencias")

    return resultadoProy


