from django.shortcuts import render

from rest_framework import generics
from .models import Users
from .serializer import UsersSerializer

class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
'''
@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    serialized = UsersSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)'''