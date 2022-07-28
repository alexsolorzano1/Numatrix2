from rest_framework import serializers, status
import rest_framework
from apps.user.views import Profile
from .models import *
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response

# User Serializer

class DiseasesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Diseases
        fields = '__all__'

class Physical_ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Physical_Activity
        fields = '__all__'

class SymptomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = '__all__'

class Eating_PlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Eating_Plan
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny]
    class Meta:
        model = Profile
        fields = [
            'id',
            'dni',
            'name',
            'last_name',
            'age',
            'weight',
            'height',
            'phone',
            'birthday',
            'is_superuser'
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only= True)
    permission_classes = [AllowAny]
    class Meta:
        model = Profile
        fields = ['email','username','password','password2','name','last_name','dni','age','weight','height','phone','birthday']
        extra_kwargs = {
                'password':{'write_only': True}
        }

    def save(self):
        account = Profile(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            name = self.validated_data['name'],
            last_name = self.validated_data['last_name'],
            dni = self.validated_data['dni'],
            age = self.validated_data['age'],
            weight = self.validated_data['weight'],
            height = self.validated_data['height'],
            phone = self.validated_data['phone'],
            birthday = self.validated_data['birthday']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Password must match.'})
        account.set_password(password)
        account.save()
        return account