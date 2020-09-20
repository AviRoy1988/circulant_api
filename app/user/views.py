from django.shortcuts import render
from django.urls import path
from rest_framework import generics
from user.serealizers import UserSerealizer

# Create your views here.

class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerealizer
