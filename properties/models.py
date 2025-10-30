from django.db import models
from django.contrib.auth.models import User

class Apartment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apartments')
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    image = models.ImageField(upload_to='apartments/')
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
