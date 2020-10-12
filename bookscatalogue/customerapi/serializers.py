from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from rest_framework.permissions import IsAuthenticated
from .models import CustomerProfile

class CustomerSerializer(CountryFieldMixin, serializers.ModelSerializer):
    
    class Meta:
        model = CustomerProfile
        fields = ('first_name', 'email', 'country')
        

