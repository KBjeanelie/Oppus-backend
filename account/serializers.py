from rest_framework import serializers
from account.models import Profil, User



class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']
    



class UserRegistrationClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['email', 'username', 'tel', 'password']

    def create(self, validate_data):
        return User.objects.create_clientuser(**validate_data)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'