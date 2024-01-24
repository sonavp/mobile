from django.db import models

class MobileDevice(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    



