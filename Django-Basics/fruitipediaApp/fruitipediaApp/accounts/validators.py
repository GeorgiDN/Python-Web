import re

from django.core.exceptions import ValidationError


def validate_letters(value):
    if not re.match(r'^[A-Za-z]', value):
        raise ValidationError('Fruit name should contain only letters!')


def validate_first_letter(value):
    if not re.match(r'^[A-Za-z]', value):
        raise ValidationError('Your name must start with a letter!')
