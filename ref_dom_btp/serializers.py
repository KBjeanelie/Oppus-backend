from rest_framework import serializers
from ref_dom_btp.models import Domaine, Metier, Travaux

class TravauxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Travaux
        fields = '__all__'


class DomaineSerializer(serializers.ModelSerializer):
    
    travaux_set = TravauxSerializer(many=True, read_only=True)
    
    image = serializers.ImageField(max_length=None, use_url=True, required=False)
    
    class Meta:
        model = Domaine
        fields = ['id', 'nom_domaine', 'image', 'travaux_set']



class MetierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metier
        fields = '__all__'