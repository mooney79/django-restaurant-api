from django.db import models

# Create your models here.

class Menuitem(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    priceCents = models.PositiveIntegerField()
    priceStr = models.CharField(max_length=255)

    def __str__(self):
        return self.name