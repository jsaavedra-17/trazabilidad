from django.db import models


# Create your models here.

class Tuercas(models.Model):

    tipo = models.CharField(max_length=30)
    medida = models.CharField(max_length=10)
    acabado = models.CharField(max_length=15)
    date_torq = models.DateField(null=True)
    nodo = models.IntegerField(null=True)
    estado = models.BooleanField(null=True)
    proyecto = models.CharField(max_length=15, null=True)
    ID = models.IntegerField(null=True)


    def __str__(self):
        return 'tipo: %s , medida: %s \n'%(self.tipo, self.medida)