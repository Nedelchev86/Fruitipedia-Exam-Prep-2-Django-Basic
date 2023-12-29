from django.core.exceptions import ValidationError


def only_letter_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Fruit name should contain only letters!")