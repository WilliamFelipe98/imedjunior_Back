from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)    
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    login = models.CharField(max_length=15, unique=True)
    senha = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.nome