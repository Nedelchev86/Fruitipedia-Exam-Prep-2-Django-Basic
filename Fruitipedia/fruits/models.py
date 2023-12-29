from django.core.validators import MinLengthValidator
from django.db import models

from Fruitipedia.fruits.validators import only_letter_validator
from Fruitipedia.profiles.models import Profile


# Create your models here.
class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        validators=[MinLengthValidator(2), only_letter_validator]
    )
    image_url = models.URLField(),
    description = models.TextField()
    nutrition = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, blank=True, null=True)
