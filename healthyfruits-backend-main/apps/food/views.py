from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
# Create your views here.

class Food_API(viewsets.ModelViewSet):

    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

class Meal_API(viewsets.ModelViewSet):

    queryset = Meal.objects.all()
    serializer_class = MealSerializers
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

class Food_Meal_API(viewsets.ModelViewSet):

    queryset = Food_Meal.objects.all()
    serializer_class = Food_MealSerializers
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

class TypeFood_API(viewsets.ModelViewSet):

    queryset = TypeFood.objects.all()
    serializer_class = TypeFoodSerializers
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

class HistoryFood_API(viewsets.ModelViewSet):

    queryset = History_Food.objects.all()
    serializer_class = HistoryFoodSerializers
    permission_classes = [AllowAny]
    filter_fields = ['id_user']