from rest_framework import serializers
from . import models

class DespesaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Despesa