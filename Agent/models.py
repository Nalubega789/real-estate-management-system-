from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='Agent/', blank=True, null=True)
    bio = models.TextField(blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
def __str__(self):
 return self.name



