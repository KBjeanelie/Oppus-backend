from rest_framework import serializers
from account.models import Employeur, Gestionnaire, User, Worker
from gest_qual_ouvrier.models import Experience, Formation
from gest_qual_ouvrier.serializers import ExperienceSerializer, FormationSerializer
from ref_dom_btp.models import Metier
from ref_dom_btp.serializers import MetierSerializer

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        # Vérifiez si l'email et le mot de passe sont fournis
        if not email:
            raise serializers.ValidationError('Email is required to login')
        if not password:
            raise serializers.ValidationError('Password is required to login')

        # Vérifiez si l'utilisateur existe dans la base de données
        user = User.objects.filter(email=email).first()
        if user is None:
            raise serializers.ValidationError('Invalid email or password')

        # Vérifiez si le mot de passe est correct
        if not user.check_password(password):
            raise serializers.ValidationError('Invalid email or password')

        data['user'] = user
        return data


class WorkerLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Worker
        fields = ['email', 'password']

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        # Vérifiez si l'email et le mot de passe sont fournis
        if not email:
            raise serializers.ValidationError('Email is required to login')
        if not password:
            raise serializers.ValidationError('Password is required to login')

        # Vérifiez si l'utilisateur existe dans la base de données
        user = Worker.objects.filter(email=email).first()
        if user is None:
            raise serializers.ValidationError('Invalid email or password')

        # Vérifiez si le mot de passe est correct
        if not user.check_password(password):
            raise serializers.ValidationError('Invalid email or password')

        data['worker'] = user
        return data


class EmployeurRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employeur
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        employeur = Employeur.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return employeur


class WorkerRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ['email', 'username', 'password', 'metier']

    def create(self, validated_data):
        worker = Worker.objects.create_worker(**validated_data)
        return worker

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class WorkerSerializer(serializers.ModelSerializer):
    metier = MetierSerializer()
    experiences = serializers.SerializerMethodField()
    formations = serializers.SerializerMethodField()
    class Meta:
        model = Worker
        fields = '__all__'
        
    def get_experiences(self, worker):
        experiences = Experience.objects.filter(worker=worker)
        serializer = ExperienceSerializer(experiences, many=True)
        return serializer.data
    
    def get_formations(self, worker):
        formations = Formation.objects.filter(worker=worker)
        serializer = FormationSerializer(formations, many=True)
        return serializer.data

class EmployeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeur
        fields = '__all__'


class GestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestionnaire
        fields = '__all__'