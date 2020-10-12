from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import CustomerProfile
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):

    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerSerializer

