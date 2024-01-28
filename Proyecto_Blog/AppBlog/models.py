from django.db import models
from django.contrib.auth.models import User
    
class Games(models.Model):
    
    def __str__(self):
        
        return f"{self.TituloGame}"
    
    TituloGame = models.CharField(max_length = 200)
    GeneroGame = models.CharField(max_length = 100)
    BreveExp = models.CharField(max_length = 100000)
    
class Manga(models.Model):
    
    def __str__(self):
        
        return f"{self.TituloManga}"
    
    TituloManga = models.CharField(max_length = 200)
    GeneroManga = models.CharField(max_length = 100)
    BreveExp = models.CharField(max_length = 100000)
    
class AvatarImagen(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    
    def __str__(self):
        return f"{self.usuario} --- {self.imagen}"