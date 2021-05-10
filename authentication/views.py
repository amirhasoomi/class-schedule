from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Profile
from .serializers import (RegisterSerializer, LoginSerializer,
                          ChangePasswordSerializer, ProfileSerializer)


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer


class ChangePasswordView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        return self.request.user.profile
