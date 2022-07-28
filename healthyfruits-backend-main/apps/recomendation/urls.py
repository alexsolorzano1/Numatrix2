from django.urls import path
from apps.recomendation.views import View_Recomendation_API, ListViewRecomendatios
from . import views

urlpatterns = [
    path('', View_Recomendation_API.as_view(),name='list'),
    path('listData', ListViewRecomendatios.as_view(),name='listRecomender'),
]