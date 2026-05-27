from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    intensidad_horaria = models.IntegerField()
    nivel = models.CharField(max_length=15)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre