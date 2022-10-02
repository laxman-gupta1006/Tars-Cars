from django.db import models

class CarService(models.Model):
    car_name = models.CharField(max_length=30)
    owner_name= models.CharField(max_length=30)
    car_model = models.CharField(max_length=255)
    service_date = models.DateTimeField()
    service_details = models.CharField(max_length=255)
    service_bill=models.IntegerField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    contact=models.IntegerField()
