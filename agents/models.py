from django.db import models
from django.contrib.auth.models import User



class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    inquiry_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name