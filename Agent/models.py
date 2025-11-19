from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, default="Real Estate Agent")
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    specialization = models.CharField(max_length=200, blank=True)
    years_experience = models.IntegerField(default=0)
    license_number = models.CharField(max_length=50, blank=True)
    properties_sold = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.title}" if self.name else f"{self.user.username} - {self.title}"

    @property
    def specialization_list(self):
        if self.specialization:
            return [spec.strip() for spec in self.specialization.split(',')]
        return []