from django.db import models
from apps.user.models import Profile

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50,null=True)
    
class Meal(models.Model):
    recipe_name = models.TextField(null=True)
    image_url = models.TextField(null=True)
    ingredients = models.TextField(null=True)
    nutrition = models.TextField(null=True)

class TypeFood(models.Model):
    name = models.CharField(max_length=50,null=True)

class Food_Meal(models.Model):
    id_food = models.ForeignKey(Food,related_name='idFood',on_delete=models.CASCADE)
    id_meal = models.ForeignKey(Meal,related_name='idMeal',on_delete=models.CASCADE)
    id_type_food = models.ForeignKey(TypeFood,related_name='idTypeFood',on_delete=models.CASCADE)

class History_Food(models.Model):

    id_user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    id_foodmeal = models.TextField(null=True)
    calories = models.DecimalField(max_digits=20, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
