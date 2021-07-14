from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Trabajo(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_problema = models.DateField()
    imagen = models.ImageField(upload_to="servicios", null=True)

    def __str__(self):
        return self.nombre