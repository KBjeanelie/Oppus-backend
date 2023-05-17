from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ref_dom_btp.serializers import MetierSerializer
from .models import Metier
from rest_framework import viewsets
from .models import Domaine, Travaux
from .serializers import DomaineSerializer, TravauxSerializer


class MetierViewSet(viewsets.ModelViewSet):
    queryset = Metier.objects.all()
    serializer_class = MetierSerializer


class DomaineViewSet(viewsets.ModelViewSet):
    queryset = Domaine.objects.all()
    serializer_class = DomaineSerializer


class TravauxViewSet(viewsets.ModelViewSet):
    queryset = Travaux.objects.all()
    serializer_class = TravauxSerializer