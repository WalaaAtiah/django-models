from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
    name =models.CharField(max_length=64,help_text="the name of the snacks",default="snack")
    purchaser= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description =models.TextField(default="description")
    image=models.TextField(default= "no image provided")

    def __str__(self):
        return self.name

# Create your models here.
