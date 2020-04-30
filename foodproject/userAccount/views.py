from django.shortcuts import render

from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializer
from .models import UserProfile
# Create your views here.



class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.ProfileSerializer
    queryset = UserProfile.objects.all()