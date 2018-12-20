from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    login = models.CharField(max_length=15, unique=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    senha = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.nome
'''
class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=15, unique=True)
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    senha = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    def __str__(self):
        return self.nome    '''