from django.db import models
from autores.models import Autores
from categorias.models import Categoria

# Create your models here.
class Libro(models.Model):
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)
    fecha_pub = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now=True)
