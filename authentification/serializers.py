from rest_framework import serializers
from account.models import Employeur, User, Worker

class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']


class EmployeurRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeur
        fields = ['email', 'username', 'password']
    
    def create(self, validate_data):
        return Employeur.objects.create_user(**validate_data)

class WorkerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['email', 'username', 'metier', 'password']
    
    def create(self, validate_data):
        return Worker.objects.create_worker(**validate_data)