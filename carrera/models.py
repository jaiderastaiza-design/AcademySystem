from django.db import models

# Create your models here.
# Create your models here.
class Carrera(models.Model):
    nombre = models.TextField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    duracion = models.IntegerField()
    modalidad = models.CharField(max_length=10)
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre