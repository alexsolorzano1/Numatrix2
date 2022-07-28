from apps.food.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('food', Food_API)
router.register('meal', Meal_API)
router.register('typefood',TypeFood_API)
router.register('food_meal', Food_Meal_API)
router.register('history_food', HistoryFood_API)

urlpatterns = router.urls