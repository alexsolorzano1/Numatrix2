from rest_framework import serializers
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import *

class FoodSerializers(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'

class MealSerializers(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = []

class Food_MealSerializers(serializers.ModelSerializer):

    class Meta:       
        model = Food_Meal
        fields = '__all__'

class TypeFoodSerializers(serializers.ModelSerializer):

    class Meta: 
        model = TypeFood
        fields = '__all__'

class HistoryFoodSerializers(serializers.ModelSerializer):
    
    class Meta: 
        model = History_Food
        fields = '__all__'

