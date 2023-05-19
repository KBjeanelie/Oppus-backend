from account.models import Employeur, Worker
from rest_framework import viewsets
from account.serializers import EmployeurSerializer, WorkerSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all().order_by('-nombre_jobs')
    serializer_class = WorkerSerializer


class EmployeurViewSet(viewsets.ModelViewSet):
    queryset = Employeur.objects.all()
    serializer_class = EmployeurSerializer
