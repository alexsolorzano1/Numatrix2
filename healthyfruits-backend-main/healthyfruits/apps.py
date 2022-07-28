from apps.user.apps import UserConfig
from apps.food.apps import FoodConfig
from apps.recomendation.apps import RecomendationConfig
from apps.ratings.apps import RatingsConfig

class UserAppConfig(UserConfig):
    name = 'apps.user'
    verbose_name = 'usuario'

class FoodAppConfig(FoodConfig):
    name = 'apps.food'
    verbose_name = 'comida'

class RatingsAppConfig(RatingsConfig):
    name = 'apps.ratings'
    verbose_name = 'rating'

class RecomendationsAppConfig(RecomendationConfig):
    name = 'apps.recomendation'
    verbose_name = 'recomendation'