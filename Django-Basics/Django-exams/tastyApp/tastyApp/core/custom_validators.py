from django.core.exceptions import ValidationError


def validate_capitalized(value):
    if not value[0].isupper():
        raise ValidationError("Name must start with a capital letter!")
