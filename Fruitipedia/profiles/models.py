from django.core.validators import MinLengthValidator
from django.db import models

from Fruitipedia.profiles.validators import validate_firs_letter


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2),
            validate_firs_letter,
        ]
    )

    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(1),
            validate_firs_letter,
        ]
    )

    email = models.EmailField(max_length=40)
    password = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(8)],
        help_text="*Password length requirements: 8 to 20 characters",

    )

    image_url = models.URLField(blank=True, null=True)
    age = models.IntegerField(null=True, blank=True, default=18)


