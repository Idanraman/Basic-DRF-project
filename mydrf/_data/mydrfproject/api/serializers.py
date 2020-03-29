from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        #exclude = ['email']
        #fields = ['url', 'username', 'email', 'groups']


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalBreed
        fields = '__all__'
        #exclude = ['email']
        #fields = ['url', 'username', 'email', 'groups']


class BreedLessSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalBreed
        fields = ['name','voice']


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
        #exclude = ['email']
        #fields = ['url', 'username', 'email', 'groups']