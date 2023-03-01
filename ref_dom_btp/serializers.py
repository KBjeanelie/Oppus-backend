from rest_framework import serializers
from ref_dom_btp.models import Domaine, Metier, Travaux

class TravauxSerializer(serializers.ModelSerializer):
    
    id_domaine = serializers.StringRelatedField()
    
    class Meta:
        model = Travaux
        fields = ['id', 'nom_travaux', 'id_domaine']


class DomaineSerializer(serializers.ModelSerializer):
    
    travaux_set = TravauxSerializer(many=True, read_only=True)
    
    class Meta:
        model = Domaine
        fields = ['id', 'nom_domaine', 'travaux_set']






class MetierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metier
        fields = ['id', 'nom_metier']