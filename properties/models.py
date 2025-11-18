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


class Booking(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)  # Changed to lowercase
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} booked {self.apartment.title}"  # Changed to apartmentz