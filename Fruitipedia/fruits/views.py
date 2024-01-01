from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from Fruitipedia.fruits.forms import DeleteFruitForm, CreateFruitForm
from Fruitipedia.fruits.models import Fruit
from Fruitipedia.profiles.models import Profile


# Create your views here.

class CreateFruitView(CreateView):
    form_class = CreateFruitForm

    template_name = "fruits/create-fruit.html"
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        # Set the owner field to the only existing Profile
        form.instance.owner = Profile.objects.first()
        return super().form_valid(form)


class DetailsFruitView(DeleteView):
    model = Fruit
    template_name = "fruits/details-fruit.html"


class EditFruitView(UpdateView):
    model = Fruit
    fields = ['name', 'image_url', 'description', 'nutrition']

    template_name = "fruits/edit-fruit.html"
    success_url = reverse_lazy('dashboard')



# TO DO FORM WITH DISABLED FILEDS
# class DeleteFruitView(DeleteView):
#     model = Fruit
#     # form_class = DeleteFruitForm
#
#     template_name = "fruits/delete-fruit.html"
#     success_url = reverse_lazy('dashboard')

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = DeleteFruitForm(instance=self.get_object())
    #     return self.render_to_response(self.get_context_data(form=form))

def delete_fruit_form(request, pk):

    fruit = Fruit.objects.get(pk=pk)

    if request.method == 'POST':

        fruit.delete()
        return redirect('dashboard')

    form = DeleteFruitForm(instance=fruit)
    context = {
        "form": form,
        "fruit": fruit,
    }
    return render(request, "fruits/delete-fruit.html", context)