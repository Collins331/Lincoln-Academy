from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    subject = models.CharField(max_length=200, blank=False)
    message = models.TextField(blank=False)