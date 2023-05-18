from account.models import Employeur, Worker
from rest_framework import viewsets
from account.serializers import EmployeurSerializer, WorkerSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

# Generate Token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }

# Custom Token Obtain Pair View
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmployeurSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all().order_by('-nombre_jobs')
    serializer_class = WorkerSerializer


class EmployeurViewSet(viewsets.ModelViewSet):
    queryset = Employeur.objects.all()
    serializer_class = EmployeurSerializer
