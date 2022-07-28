from django.db import models
from apps.user.models import Profile

# Create your models here.
class RecomendationModel(models.Model):
    id_user = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)   
    id_recipe = models.TextField(null=True)
    recomendation_food = models.JSONField()

    
