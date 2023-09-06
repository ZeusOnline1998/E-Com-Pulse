from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import CustomUser

# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Create your views here.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),  # type: ignore
    }

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        email = request.data['email']
        password = request.data['password']
        user = authenticate(email=email, password=password)
        print(user)
        if user:
            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)
            return Response({
                'access': str(access),
                'refresh': str(refresh),
            })
        # else:
    return Response({"error": "Invalid Credentials"})

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user_details(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        'full_name': user.get_full_name(),
    }
    return Response(context)
