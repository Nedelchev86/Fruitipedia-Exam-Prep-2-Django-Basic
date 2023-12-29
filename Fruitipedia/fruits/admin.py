from django.contrib import admin

from Fruitipedia.fruits.models import Fruit


# Register your models here.
@admin.register(Fruit)
class AdminFruit(admin.ModelAdmin):
    pass