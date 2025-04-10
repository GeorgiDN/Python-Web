import re

from django.core.exceptions import ValidationError


def validate_username(value):
    if not re.match(r'^[A-Za-z0-9_]', value):
        raise ValidationError("Username must contain only letters, digits, and underscores!")


def validate_year(value):
    if not (1999 <= value <= 2030):
        raise ValidationError("Year must be between 1999 and 2030!")
