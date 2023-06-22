from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class Estado(models.Model):
    idEstado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.estado)

class Articulo(models.Model):
    idArticulo = models.AutoField(primary_key=True)
    articulo = models.CharField(max_length=255)
    descripcion = models.TextField(default="")
    imagen = models.ImageField(upload_to='img/')
    idUsuario = models.ForeignKey(User,on_delete=models.CASCADE)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE,default=1)

    def __str__(self):
        return str(self.articulo)