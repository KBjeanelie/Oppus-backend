from rest_framework import serializers
from .models import Competence, Formation, Experience


class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'


# class EtablissementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Etablissement
#         fields = '__all__'


# class DiplomeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Diplome
#         fields = '__all__'


# class DomaineEtudeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Domaine_Etude
#         fields = '__all__'
