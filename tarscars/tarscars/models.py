from django.db import models

class Contactus(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=255)