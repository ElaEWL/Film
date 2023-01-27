from rest_framework import serializers
from .models import Aktor, Rezyser, Film, Ocena, Kategoria
from django.contrib.auth.models import User 
from rest_framework.authtoken.models import Token

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id','nazwa', 'kategoria','opis','rok_produkcji']
        
class AktorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aktor
        fields = ['id','imię', 'nazwisko']
        
class RezyserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezyser
        fields = ['id','imię', 'nazwisko']
        
class KategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoria
        fields = ['id','nazwa','opis']  
        
class OcenaSerializer(serializers.ModelSerializer):
    user_nazwisko = serializers.ReadOnlyField(source='user.first_name')
    username = serializers.ReadOnlyField(source='user.username')
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Ocena
        fields = ['id','wartość', 'user', 'user_nazwisko', 'username', 'film','published_date']      

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
                }
            }
    
    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user
        
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)    