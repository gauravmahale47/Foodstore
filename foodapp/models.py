from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.

class Food(models.Model):
    food_Id = models.BigAutoField(primary_key=True)
    food_Name = models.CharField(max_length=30)
    food_Type = models.CharField(max_length=30)
    food_Price = models.FloatField()
    food_Description = models.TextField()
    # food_Image = models.ImageField(upload_to='Food/', default="") 

    def __str__(self):
        return f'{self.food_Name} - {self.food_Type}'
