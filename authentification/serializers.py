from rest_framework import serializers
from account.models import Employeur, User

class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']


class EmployeurRegister(serializers.ModelSerializer):
    class Meta:
        model = Employeur
        fields = ['email', 'username', 'password']
    
    def create(self, validate_data):
        return Employeur.objects.create_user(**validate_data)