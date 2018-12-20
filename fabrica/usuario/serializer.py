from rest_framework import serializers
from . import models
from despesa.serializer import DespesaSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    #despesas = serializers.StringRelatedField(many=True)
    despesas = DespesaSerializer(many=True, read_only=True)
   
    class Meta:
        fields = '__all__'
        model = models.Usuario
'''
    def create(self, validated_data):
        user = super(UsuarioSerializer, self).create(validated_data)
        user.set_password(validated_data['senha'])
        user.save()
        return user'''
