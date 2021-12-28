from django.db import models


# Create your models here.
class Union(models.Model):

    fecha_union = models.DateField(auto_now_add=False)
    hora_union = models.CharField(max_length=50)
    id_union = models.CharField(max_length=50, primary_key=True)
    referencia = models.CharField(max_length=50)

    def __str__(self):
        return 'tipo: %s , medida: %s \n'%(self.tipo, self.medida)

class Perno(models.Model):

    fecha_perno = models.CharField(max_length=50)
    tiempo = models.CharField(max_length=50)
    id_perno = models.CharField(max_length=50, primary_key=True)
    estado_perno = models.CharField(max_length=50)
    union_perno = models.ForeignKey(Union, on_delete= models.CASCADE)

class Estado(models.Model):
    descrip_estado = models.CharField(max_length=50)
    salida_union = models.ForeignKey(Union, on_delete=models.CASCADE)
    salida_perno = models.ForeignKey(Perno, on_delete=models.CASCADE)


class CodigoSalida(models.Model):

    descrip_codigo = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)