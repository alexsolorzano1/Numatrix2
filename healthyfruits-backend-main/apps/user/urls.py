from os import name
from apps.user.views import Diseases_API, Eating_Plan_API, Physical_Activity_API, Profile_API, Symptom_API,UserActiveAPI, registration_view
from rest_framework import routers
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url

router = routers.SimpleRouter()
router.register('diseases', Diseases_API)
router.register('physical_activity', Physical_Activity_API)
router.register('symptom', Symptom_API)
router.register('eating_plan', Eating_Plan_API)
router.register('profile', Profile_API)

urlpatterns = router.urls

urlpatterns += [
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    url(r'^active/', UserActiveAPI.as_view(), name='api_user_active'),
]