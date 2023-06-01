from rest_framework.decorators import action
from rest_framework.response import Response
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
    
    @action(detail=True, methods=['GET'])
    def by_domaine(self, request, pk=None):
        travaux = self.queryset.filter(id_domaine=pk)
        serializer = self.serializer_class(travaux, many=True)
        return Response(serializer.data)