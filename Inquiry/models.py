from django.db import models


class Inquiry(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    inquiry=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
