from django.core.exceptions import ValidationError

def validate_quantity(value):
    if value < 0:
        raise ValidationError('Количество не может быть отрицательным.')