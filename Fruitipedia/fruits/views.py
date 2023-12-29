from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from Fruitipedia.fruits.forms import DeleteFruitForm, CreateFruitForm
from Fruitipedia.fruits.models import Fruit


# Create your views here.

class CreateFruitView(CreateView):
    form_class = CreateFruitForm

    template_name = "fruits/create-fruit.html"
    success_url = reverse_lazy('dashboard')


class DetailsFruitView(DeleteView):
    model = Fruit
    template_name = "fruits/details-fruit.html"


class EditFruitView(UpdateView):
    model = Fruit
    fields = ['name', 'image_url', 'description', 'nutrition']

    template_name = "fruits/edit-fruit.html"
    success_url = reverse_lazy('dashboard')



# TO DO FORM WITH DISABLED FILEDS
class DeleteFruitView(DeleteView):
    model = Fruit
    # form_class = DeleteFruitForm

    template_name = "fruits/delete-fruit.html"
    success_url = reverse_lazy('dashboard')

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = DeleteFruitForm(instance=self.get_object())
    #     return self.render_to_response(self.get_context_data(form=form))


