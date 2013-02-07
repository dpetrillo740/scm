from django.db import models

class Sku(models.Model):
    sku                 =models.CharField(max_length=30, unique=True)
    title               =models.CharField(max_length=90, null=True)
    variant             =models.CharField(max_length=90, null=True)
