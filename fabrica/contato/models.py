from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    descricao = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
 
def __str__(self):
    return self.nome