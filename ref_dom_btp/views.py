from rest_framework.decorators import action
from rest_framework.response import Response
from account.models import Ouvrier
from account.serializers import WorkerSerializer
from ref_dom_btp.serializers import MetierSerializer
from rest_framework.views import APIView
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

class GetWorkerByMetier(APIView):
    def get(self, request, travaux_id):
        try:
            travaux = Travaux.objects.get(id=travaux_id)
            metiers = Metier.objects.filter(task=travaux)
            workers = Ouvrier.objects.filter(metier__in=metiers).order_by('-annee_experience')
            serializer = WorkerSerializer(workers, many=True)
            return Response(serializer.data)
        
        except Ouvrier.DoesNotExist:
            return Response({"error": "Travaux does not exist"}, status=404)
