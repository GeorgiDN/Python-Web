import re


def validate_nickname(value):
    if not re.fullmatch(r'^[A-Za-z0-9]+$', value):
        raise ValueError('Your nickname is invalid!')
