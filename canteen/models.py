from django.db import models

# Create your models here.

class FoodItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='food_pic')

    def __str__(self):
        return self.name
