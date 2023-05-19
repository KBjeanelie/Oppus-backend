from rest_framework.views import APIView
from account.serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView

from authentification.renderers import UserRenderer
from authentification.serializers import UserLoginSerializer

# Generate Token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }

# Custom Token Obtain Pair View
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserSerializer


class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    print(email, password)
    user = authenticate(email=email, password=password)
    
    if user is not None:
      token = get_tokens_for_user(user)
      return Response(token, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

