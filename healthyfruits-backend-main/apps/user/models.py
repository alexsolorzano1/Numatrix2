from django.db import models
from django.db.models import fields
from apps.user.validators import *
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# USUARIOS ──────────────────────────────────────────────────

class ProfileManager(BaseUserManager):
    '''Interfaz que proporcionan las operaciones de consulta de la base de datos para Usuarios'''
    def create_user(self, email, name, password = None):
        '''función para crear usuarios'''
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
                email=self.normalize_email(email),
                name=name,
            )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password):
        '''función para crear un super usuario (comando: createsuperuser)'''
        user = self.create_user(
                email=email,
                password=password,
                name=name,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class Profile(AbstractBaseUser):
    SEX = ((0,' '),(1,'MAN'),(2,'WOMAN'))
    
    email = models.EmailField(blank=False,unique=True,max_length=40)
    username = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=False)
    dni = models.CharField(validators=[dni], max_length=8, null=True)
    name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=True,blank=True)
    weight = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    phone = models.CharField(max_length=9, null=True)
    birthday = models.DateField(validators=[fechaNacimiento], null=True)
    type_sex = models.PositiveSmallIntegerField(blank=False,default=0,choices=SEX,
        validators = [MinValueValidator(0), MaxValueValidator(2)])
    
    is_admin = models.BooleanField(default=False,verbose_name='super administrador')
    # estado de super administrador del usuario
    is_active = models.BooleanField(default=True,verbose_name='estado')
    # estado del usuario
    is_superuser = models.BooleanField(default=False,verbose_name='super usuario')
    is_staff = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    objects = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        ordering = ['name']

    def __str__(self):
        return "%s %s" % (self.name, self.last_name)

    def edad(self):
        if self.birthday is None:
            return 0
        else:
            return int((datetime.now().date() - self.birthday).days/365.25)

    def has_perm(self, perm, obj=None): 
        return self.is_admin

    def has_module_perms(self, app_label): 
        return True

@receiver(post_save, sender= settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Diseases(models.Model):
    #Enfermedades 
    enfDiabetes = models.CharField(max_length=500,default="null")
    enfHipertension = models.CharField(max_length=500,default="null")
    enfObesidad = models.CharField(max_length=500,default="null")
    enfDislipidemias = models.CharField(max_length=500,default="null")
    enfCardiopatia = models.CharField(max_length=500,default="null")
    enfCancer = models.CharField(max_length=500,default="null")
    
class Physical_Activity(models.Model):
    #AF = ACTIVIDAD FISICA
    consumeAlcohol = models.CharField(max_length=800,null=True)
    fuma = models.CharField(max_length=800,null=True)
    otros = models.CharField(max_length=800,null=True)

class Symptom(models.Model):
    ssestrenimiento = models.CharField(max_length=20,null=True)
    ssdiarrea = models.CharField(max_length=20,null=True)
    sscefalea= models.CharField(max_length=20,null=True)
    ssvomito = models.CharField(max_length=20,null=True)
    ssfiebre = models.CharField(max_length=20,null=True)
    ssdebilidad = models.CharField(max_length=20,null=True)
    ssfaltapetito = models.CharField(max_length=20,null=True)
    ssgananciapeso = models.CharField(max_length=20,null=True)
    ssperdidapeso = models.CharField(max_length=20,null=True)
    ssedema = models.CharField(max_length=20,null=True)
    sstumoracion = models.CharField(max_length=20,null=True)
    proximaCita = models.DateField(null=True)


class Eating_Plan(models.Model):
    id_user = models.ForeignKey(Profile,related_name='idUser',on_delete=models.CASCADE)
    req_calories = models.FloatField(null = True)
    req_proteins = models.FloatField(null = True)
    req_carbohydrates = models.FloatField(null = True)
    req_fats = models.FloatField(null = True)
    req_vitamins = models.FloatField(null = True)

    def __str__(self):
        return "%s" % (self.id_user)