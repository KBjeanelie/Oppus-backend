from django.db.models import Max
from rest_framework import generics, permissions
from .models import Discussion
from .serializers import DiscussionSerializer

class DiscussionListCreateView(generics.ListCreateAPIView):
    serializer_class = DiscussionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtrer les discussions par l'utilisateur connecté et sélectionner le dernier message de chaque discussion
        queryset = Discussion.objects.filter(sender=self.request.user) | Discussion.objects.filter(receiver=self.request.user)
        queryset = queryset.values('sender', 'receiver').annotate(last_message=Max('time')).order_by('-last_message')
        return Discussion.objects.filter(time__in=queryset.values('last_message'))

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class DiscussionDetailView(generics.RetrieveAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = [permissions.IsAuthenticated]
