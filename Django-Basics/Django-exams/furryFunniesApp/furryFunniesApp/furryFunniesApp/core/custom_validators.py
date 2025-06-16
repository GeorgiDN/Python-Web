from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_letters_only(value):
    if not value.isalpha():
        raise ValidationError("Your name must contain letters only!")


passcode_validator = RegexValidator(
    regex=r'^\d{6}$',
    message="Your passcode must be exactly 6 digits!"
)
