from django.db import models

# Create your models here.
class Matricula(models.Model):
    fecha_matricula = models.DateField(auto_now_add=True)
    periodo = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    nota_final = models.DecimalField(max_digits=4, decimal_places=2)
    observaciones = models.TextField()

    def __str__(self):
        return f"{self.fecha_matricula} - {self.periodo}"