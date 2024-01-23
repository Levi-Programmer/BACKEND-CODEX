from django.db import models

# Create your models here.
class Horizon(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    

class User(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=30)
    numero_documento = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    # confirmPassword no es necesario en el modelo

    # Representación del modelo
    def __str__(self):
        return self.nombre
