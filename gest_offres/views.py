from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import Worker

from account.serializers import WorkerSerializer
from .models import Reservation, Appreciation, Offre, Commentaire
from .serializers import ReservationSerializer, AppreciationSerializer, OffreSerializer, CommentaireSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AppreciationViewSet(viewsets.ModelViewSet):
    queryset = Appreciation.objects.all()
    serializer_class = AppreciationSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        reservation_id = self.request.data.get('id_reservation')
        reservation = Reservation.objects.get(pk=reservation_id)
        if reservation.worker == self.request.user:
            serializer.save(employeur=self.request.user)
        else:
            raise('Vous n\'êtes pas autorisé à ajouter une appréciation pour cette réservation.')


class OffreViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OffreSerializer

    def get_queryset(self):
        # Récupérer l'utilisateur connecté
        employeur = self.request.user

        # Filtrer les offres par l'employeur
        queryset = Offre.objects.filter(employeur=employeur, statut=True).order_by('-created_at')
        return queryset

    def perform_create(self, serializer):
        # Associer l'employeur actuel à la nouvelle offre
        serializer.save(employeur=self.request.user)


class OffreArchiveViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OffreSerializer
    queryset = Offre.objects.all()

    def get_queryset(self):
        # Récupérer l'utilisateur connecté
        employeur = self.request.user

        # Filtrer les offres par l'employeur
        queryset = Offre.objects.filter(employeur=employeur, statut=False)

        return queryset

    def perform_create(self, serializer):
        # Associer l'employeur actuel à la nouvelle offre
        serializer.save(employeur=self.request.user)


class GetWorkerByOfferAPIView(APIView):
    
    def get(self, request, offre_id):
        # Récupérer l'objet Offre en fonction de l'offre_id
        offre = Offre.objects.get(id=offre_id)
        
        # Récupérer l'objet Travaux associé à l'Offre
        travaux = offre.id_travaux
        
        # Récupérer les objets Metier associés au Travaux
        metiers = travaux.metier.all()
        
        # Récupérer les objets Worker qui ont les objets Metier associés
        workers = Worker.objects.filter(metier__in=metiers)
        
        serializer = WorkerSerializer(workers, many=True)
        
        return Response(serializer.data)
    

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        offre_id = self.request.data.get('id_offre')
        #offre = Offre.objects.get(pk=offre_id)
        serializer.save(user=self.request.user)
        # if offre.user == self.request.user:
        #     serializer.save(user=self.request.user)
        # else:
        #     raise PermissionDenied('Vous n\'êtes pas autorisé à ajouter un commentaire à cette offre.')
