from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from Fruitipedia.common.views import get_profile
from Fruitipedia.fruits.forms import CreateProfileFrom
from Fruitipedia.fruits.models import Fruit
from Fruitipedia.profiles.models import Profile




# Create your views here.
class CreateProfileView(CreateView):
    form_class = CreateProfileFrom
    template_name = "profiles/create-profile.html"
    success_url = reverse_lazy("dashboard")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        if profile:
            have_profile = False
        else:
            have_profile = True
        context['have_profile'] = have_profile
        return context

class DetailsProfileView(DeleteView):
    def get_object(self, queryset=None):
        obj = Profile.objects.first()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Fruit.objects.all()
        return context
    template_name = "profiles/details-profile.html"


class EditProfileView(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'image_url', 'age']
    template_name = "profiles/edit-profile.html"
    success_url = reverse_lazy("details_profile")

    def get_object(self, queryset=None):
        obj = Profile.objects.first()
        return obj


class DeleteProfileView(DeleteView):
    model = Profile
    template_name = "profiles/delete-profile.html"
    success_url = reverse_lazy('HomePage')

    def get_object(self, queryset=None):
        obj = Profile.objects.first()
        return obj

    def post(self, request, *args, **kwargs):
        post = super().post(request, *args, **kwargs)
        Fruit.objects.all().delete()
        return post


