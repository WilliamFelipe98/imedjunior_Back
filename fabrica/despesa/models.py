from django.db import models
from usuario.models import Usuario 

class Despesa(models.Model):
    descricao = models.CharField(max_length=500)
    usuario = models.ForeignKey(Usuario, related_name='despesas', on_delete=models.CASCADE)
    valor = models.CharField(max_length=20)
    data = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
     
    def __str__(self):
        return "Descrição: "+self.descricao+", Valor: "+ self.valor+", Data: "+ self.data

#    usuario = models.CharField(max_length=10)
