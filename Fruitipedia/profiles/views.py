from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from Fruitipedia.fruits.forms import CreateProfileFrom
from Fruitipedia.profiles.models import Profile




# Create your views here.
class CreateProfileView(CreateView):
    form_class = CreateProfileFrom
    template_name = "profiles/create-profile.html"
    success_url = reverse_lazy("dashboard")



class DetailsProfileView(DeleteView):
    model = Profile
    template_name = "profiles/delete-profile.html"


class EditProfileView(UpdateView):
    model = Profile
    template_name = "profiles/edit-profile.html"


class DeleteProfileView(DeleteView):
    model = Profile
    template_name = "profiles/delete-profile.html"

