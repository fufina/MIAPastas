from django.db import models

# Create your models here.

class Insumo(models.Model):
    UNIDADES = (
        (1, "Kg"),
        (2, "Litro"),
        (3, "Unidad"),
        (4, "Docena"),
        (5, "Caja"),
    )
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    stock = models.PositiveIntegerField()
    unidad_medida = models.PositiveSmallIntegerField(choices=UNIDADES)

    def __str__(self):
        return self.nombre