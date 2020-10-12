from django.db import models
import datetime
from customerapi.models import CustomerProfile

class BookCatalogue(models.Model):
    email = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    date_added = models.DateField(default=datetime.date.today)
    isbn = models.CharField(max_length=13)

    class Meta:
        unique_together = ('email','isbn')

    def __str__(self):
        return self.title