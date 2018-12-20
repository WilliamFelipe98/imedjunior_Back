from django.shortcuts import render

from rest_framework import generics
from .models import Cliente
from .serializer import ClienteSerializer
from rest_framework.permissions import IsAuthenticated

class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = (IsAuthenticated,)

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = (IsAuthenticated,)
