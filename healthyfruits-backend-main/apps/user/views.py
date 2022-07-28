from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets, generics, status

from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators  import  api_view, permission_classes, authentication_classes

# Create your views here.

class Profile_API(viewsets.ModelViewSet):
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]

class Diseases_API(viewsets.ModelViewSet):

    queryset = Diseases.objects.all()
    serializer_class = DiseasesSerializers

class Physical_Activity_API(viewsets.ModelViewSet):

    queryset = Physical_Activity.objects.all()
    serializer_class = Physical_ActivitySerializers

class Symptom_API(viewsets.ModelViewSet):

    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializers

class Eating_Plan_API(viewsets.ModelViewSet):

    queryset = Eating_Plan.objects.all()
    serializer_class = Eating_PlanSerializers

class UserActiveAPI(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        response = super(UserActiveAPI, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


@api_view(['POST',])
@authentication_classes([])
@permission_classes([AllowAny])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data= request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered a new user."
            data['email'] = account.email
            data['username'] = account.username
            data['name'] = account.name
            data ['last_name'] = account.last_name
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)