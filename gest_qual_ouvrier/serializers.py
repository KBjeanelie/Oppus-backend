from rest_framework import serializers
from .models import Competence, Etablissement, Diplome, Domaine_Etude, Formation, Experience, Competence_Ouvrier


class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'


class EtablissementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etablissement
        fields = '__all__'


class DiplomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diplome
        fields = '__all__'


class DomaineEtudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domaine_Etude
        fields = '__all__'


class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class CompetenceOuvrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence_Ouvrier
        fields = '__all__'
