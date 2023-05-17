from rest_framework.views import APIView
from account.models import Employeur, Worker
from rest_framework import viewsets
from account.renderers import UserRenderer
from account.serializers import EmployeurRegistrationSerializer, EmployeurSerializer, UserLoginSerializer, WorkerRegistrationSerializer, WorkerSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

# Generate Token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }

# GET THE CURRENT USER AUTHENTICATED
class GetCurrentEmployeurView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        employeur = request.user
        serializer = EmployeurSerializer(employeur)
        return Response(serializer.data)

class GetCurrentWorkerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        worker = request.user
        serializer = WorkerSerializer(worker)
        return Response(serializer.data)

# Custom Token Obtain Pair View
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserLoginSerializer

# Create your views here.
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            token = get_tokens_for_user(user)
            return Response(token, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


class EmployeurRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = EmployeurRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employeur = serializer.save()
        token = get_tokens_for_user(employeur)
        return Response(token, status=status.HTTP_201_CREATED)


class WorkerRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = WorkerRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        worker = serializer.save()
        token = get_tokens_for_user(worker)
        return Response(token, status=status.HTTP_201_CREATED)



class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class EmployeurViewSet(viewsets.ModelViewSet):
    queryset = Employeur.objects.all()
    serializer_class = EmployeurSerializer
