from rest_framework.views import APIView
from account.renderers import UserRenderer
from account.serializers import UserLoginSerializer, UserProfileSerializer, UserRegistrationClientSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }
  
  
# GET THE CURRENT USER AUTHENTICATED
class GetCurrentUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

# Create your views here.
class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)



class UserRegistrationClientView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
      serializer = UserRegistrationClientSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      user = serializer.save()
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)



class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
      serializer = UserProfileSerializer(request.user)
      return Response(serializer.data, status=status.HTTP_200_OK)