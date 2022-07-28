from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Profile)
admin.site.register(Diseases)
admin.site.register(Physical_Activity)
admin.site.register(Symptom)
admin.site.register(Eating_Plan)