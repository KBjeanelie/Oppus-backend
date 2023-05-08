from rest_framework import serializers
from account.serializers import UserSerializer
from ref_dom_btp.serializers import DomaineSerializer, TravauxSerializer

from .models import Reservation, Offre, Appreciation, Commentaire

class AppreciationSerializer(serializers.ModelSerializer):
    employeur = UserSerializer(read_only=True)
    id_reservation = serializers.PrimaryKeyRelatedField(queryset=Reservation.objects.all())

    class Meta:
        model = Appreciation
        fields = '__all__'


class OffreSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    id_domaine = DomaineSerializer(read_only=True)
    id_travaux = TravauxSerializer(read_only=True)
    id_reservation = serializers.PrimaryKeyRelatedField(queryset=Reservation.objects.all(), required=False)

    class Meta:
        model = Offre
        fields = '__all__'


class CommentaireSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    id_offre = serializers.PrimaryKeyRelatedField(queryset=Offre.objects.all())

    class Meta:
        model = Commentaire
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    worker = UserSerializer(read_only=True)
    id_offre = OffreSerializer(read_only=True)
    id_appreciation = AppreciationSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'
