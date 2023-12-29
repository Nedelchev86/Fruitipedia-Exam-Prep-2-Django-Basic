from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView

from Fruitipedia.fruits.models import Fruit


# Create your views here.

class CreateFruitView(CreateView):
    model = Fruit
    template_name = "fruits/create-fruit.html"


class DetailsFruitView(DeleteView):
    model = Fruit
    template_name = "fruits/details-fruit.html"


class EditFruitView(UpdateView):
    model = Fruit
    template_name = "fruits/edit-fruit.html"


class DeleteFruitView(DeleteView):
    model = Fruit
    template_name = "fruits/delete-fruit.html"

