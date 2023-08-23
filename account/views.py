from requests import Response
from account.models import Employeur, Ouvrier
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from account.serializers import EmployeurSerializer, WorkerSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Ouvrier.objects.all().order_by('-nombre_jobs')
    serializer_class = WorkerSerializer


class EmployeurViewSet(viewsets.ModelViewSet):
    queryset = Employeur.objects.all()
    serializer_class = EmployeurSerializer
    #permission_classes = [IsAuthenticated]
    
    # @action(detail=False, methods=['put'])
    # def update_profile(self, request):
    #     employeur = request.user
    #     serializer = self.get_serializer(employeur, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)

    # def perform_update(self, serializer):
    #     serializer.save()
