from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    season = models.CharField(max_length=50)
    favorable_weather = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    amount = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)


    def calculate_total(self):
        return self.price * self.amount

    def __str__(self):
        return self.name
