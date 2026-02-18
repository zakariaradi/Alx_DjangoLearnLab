from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from accounts.serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    def post(self, request):
        user = authenticate(
            username=request.data['username'],
            password=request.data['password']
        )
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=400)

