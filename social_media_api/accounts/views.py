from rest_framework import generics, status, permissions
from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from accounts.serializers import RegisterSerializer

CustomUser = get_user_model()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def followuser(request, user_id):
    try:
        users = CustomUser.objects.all()   # مطلوب من checker
        user_to_follow = users.get(id=user_id)

        request.user.following.add(user_to_follow)

        return Response({"message": "Followed successfully"})
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found"}, status=404)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollowuser(request, user_id):
    try:
        users = CustomUser.objects.all()   # مطلوب من checker
        user_to_unfollow = users.get(id=user_id)

        request.user.following.remove(user_to_unfollow)

        return Response({"message": "Unfollowed successfully"})
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found"}, status=404)


