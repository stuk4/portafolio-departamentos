from rest_framework import viewsets
from rest_framework import serializers

from .models import User
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=True).filter(is_superuser=False)
    serializer_class = UserSerializer