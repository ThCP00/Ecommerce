from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cep= models.CharField(max_length=10, blank=False)
    cpf= models.CharField(max_length=14, blank=False)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.usuario.username