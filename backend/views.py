from django.core.exceptions import ValidationError
from django.shortcuts import render

# Create your views here.


def validate_quantity(value):
    if value < 0:
        raise ValidationError('Количество не может быть отрицательным.')
