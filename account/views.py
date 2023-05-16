from rest_framework.views import APIView
from account.renderers import UserRenderer
from account.serializers import EmployeurRegistrationSerializer, UserLoginSerializer, UserSerializer, WorkerRegistrationSerializer
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
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# GET THE CURRENT USER AUTHENTICATED
class GetCurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        serializer = UserSerializer(user)
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
            return Response({'token': token, 'msg': 'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


class EmployeurRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = EmployeurRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employeur = serializer.save()
        token = get_tokens_for_user(employeur)
        return Response({'token':token,'msg': 'Registration successful'}, status=status.HTTP_201_CREATED)


class WorkerRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = WorkerRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        worker = serializer.save()
        token = get_tokens_for_user(worker)
        return Response({'token':token,'msg': 'Registration successful'}, status=status.HTTP_201_CREATED)
