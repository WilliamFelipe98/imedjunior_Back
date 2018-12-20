from rest_framework import serializers
from . import models
from despesa.serializer import DespesaSerializer

class UsersSerializer(serializers.ModelSerializer):
    #despesas = serializers.StringRelatedField(many=False)
    class Meta:
        fields = '__all__'
        model = models.Users
'''
    def create(self, validated_data):
        user = super(UsersSerializer, self).create(validated_data)
        user.set_password(validated_data['senha'])
        user.save()
        return user'''

'''class UserSerializer(serializers.ModelSerializer):
    password = serializers.Cha(rField(write_only=True)

    class Meta:
        model = models.User
        fields = '__all__'
    
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user'''