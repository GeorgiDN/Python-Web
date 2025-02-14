import re

from django.core.exceptions import ValidationError


def validate_nickname(value):
    if not re.fullmatch(r'^[A-Za-z0-9]+$', value):
        raise ValidationError('Your nickname is invalid!')
