from rest_framework import viewsets, permissions
from .models import Reservation, Appreciation, Offre, Commentaire
from .serializers import ReservationSerializer, AppreciationSerializer, OffreSerializer, CommentaireSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AppreciationViewSet(viewsets.ModelViewSet):
    queryset = Appreciation.objects.all()
    serializer_class = AppreciationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        reservation_id = self.request.data.get('id_reservation')
        reservation = Reservation.objects.get(pk=reservation_id)
        if reservation.worker == self.request.user:
            serializer.save(employeur=self.request.user)
        else:
            raise('Vous n\'êtes pas autorisé à ajouter une appréciation pour cette réservation.')


class OffreViewSet(viewsets.ModelViewSet):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OffreArchiveViewSet(viewsets.ModelViewSet):
    queryset = Offre.objects.filter(statut=False)
    serializer_class = OffreSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        offre_id = self.request.data.get('id_offre')
        #offre = Offre.objects.get(pk=offre_id)
        serializer.save(user=self.request.user)
        # if offre.user == self.request.user:
        #     serializer.save(user=self.request.user)
        # else:
        #     raise PermissionDenied('Vous n\'êtes pas autorisé à ajouter un commentaire à cette offre.')
