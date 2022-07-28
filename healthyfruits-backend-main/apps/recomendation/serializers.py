from rest_framework import serializers
from .models import RecomendationModel
from apps.food.models import Meal

class RecomendationSerializers(serializers.ModelSerializer):
    class Meta:
        model = RecomendationModel
        fields = ['id_recipe','recomendation_food']      

class ListAPISerializers(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'