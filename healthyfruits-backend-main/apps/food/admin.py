from django.contrib import admin
from django.contrib.admin.helpers import AdminErrorList
from apps.food.models import *
# Register your models here.

admin.site.register(Food)
admin.site.register(Meal)
admin.site.register(Food_Meal)
admin.site.register(TypeFood)
admin.site.register(History_Food)
