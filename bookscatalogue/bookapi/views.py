from django.shortcuts import render
from django.http import Http404, HttpResponse
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .serializers import BookSerializer
from .models import BookCatalogue, CustomerProfile
import urllib.request

class BookDateFilter(filters.FilterSet):
    
    # date = filters.DateFilter()
    date_added = filters.DateRangeFilter()
    
    class Meta:
        model = BookCatalogue
        fields = ['date_added']
        # fields = {
        #     'date_added'
        #     #  'date_added':('lte', 'gte')
        # }

class BookViewSet(viewsets.ModelViewSet):
    
    # queryset = BookCatalogue.objects.all()
    serializer_class = BookSerializer    
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = BookDateFilter

    def get_queryset(self):
        username = self.request.user
        # print(username)
        if (CustomerProfile.objects.get(email=username)):
            user = CustomerProfile.objects.get(email=username)
            print(user)
            return (BookCatalogue.objects.filter(email=user))
        return HttpResponse("Please Login to check the books")

   