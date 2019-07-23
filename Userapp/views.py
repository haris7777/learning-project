from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
from rest_framework import viewsets


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
from django.shortcuts import render
from rest_framework import generics
#
#
# class UserView(generics.CreateAPIView):
#     def get_queryset(self):
#         return UserView.objects.all()
#
#
# class ProfileView(generics.CreateAPIView):
#     def get_queryset(self):
#         return ProfileView.objects.all()



