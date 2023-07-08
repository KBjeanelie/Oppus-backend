from rest_framework import serializers
from account.models import Employeur, Gestionnaire, User, Worker
from gest_qual_ouvrier.models import Competence, Experience, Formation
from gest_qual_ouvrier.serializers import CompetenceSerializer, ExperienceSerializer, FormationSerializer
from ref_dom_btp.serializers import MetierSerializer, TravauxSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class WorkerSerializer(serializers.ModelSerializer):
    metier = MetierSerializer()
    canDo = TravauxSerializer(many=True)
    experiences = serializers.SerializerMethodField()
    formations = serializers.SerializerMethodField()
    competences = serializers.SerializerMethodField()
    
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
    
    def get_competences(self, worker):
        competences = Competence.objects.filter(workers=worker)
        serializer = CompetenceSerializer(competences, many=True)
        return serializer.data

class EmployeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeur
        fields = '__all__'


class GestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestionnaire
        fields = '__all__'

