from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import update_session_auth_hash

class UserSerializer(serializers.ModelSerializer):
    #Configuración para encriptar contraseña al crear usuario
    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active=validated_data['is_active'],
            is_staff=validated_data['is_staff'],
            telefono=validated_data['telefono'],
            edad=validated_data['edad'],
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    #Configuración para encriptar contraseña al modificar usuario
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.edad = validated_data.get('edad', instance.edad)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        password = validated_data.get('password', None)
        instance.set_password(password)
        instance.save()
        update_session_auth_hash(self.context.get('request'), instance)
        return instance

    #Agrego id para solo mostrarlo en el api
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ["id", "first_name","last_name", "is_active", "is_staff","telefono", "edad", "username", "email", "password"]
