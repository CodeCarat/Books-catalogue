from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from rest_framework.permissions import IsAuthenticated
from .models import BookCatalogue, CustomerProfile
from rest_framework.authtoken.models import Token
import requests
from django.conf import settings


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BookCatalogue
        fields = ('id', 'email', 'title', 'author', 'date_added', 'isbn')
        permission_classes = [IsAuthenticated]

    def validate(self, data):
        isbn_no = data['isbn']
        print(isbn_no)
        parms = {"q":isbn_no+'isbn', 'key':settings.API_KEY}
        res = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        print(res.url)
        print(res.ok)
        if not (res.ok):
            raise serializers.ValidationError(
            {"isbn": "Please enter a valid ISBN"}
        ) 
        return data
        # headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    