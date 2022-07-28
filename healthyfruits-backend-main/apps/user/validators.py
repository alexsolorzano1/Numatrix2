from django.core.exceptions import ValidationError
from datetime import datetime


def fechaNacimiento(value):
    a = int((datetime.now().date() - value).days / 365.25)
    b = int((datetime.now().date() - value).days)
    if not (0 <= a < 130) & (b >= 0):
        raise ValidationError('datos de fecha no invalidos')


def dni(value):
    if not len(value) == 8:
        raise ValidationError('dni deberia contener 8 caracteres')


def energiaAl(value):
    if not value >= 0 & value < 10000:
        raise ValidationError('ingrese una medida correcta max xxxx')
