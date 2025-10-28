from django.db import models

# Create your models here.
class Inquiries(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    inquiry=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
