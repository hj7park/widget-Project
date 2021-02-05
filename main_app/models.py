from django.db import models

# Create your models here.


class Widget(models.Model):
    description = models.CharField(max_length=200 ,null=True)
    quantity = models.IntegerField(null=True)