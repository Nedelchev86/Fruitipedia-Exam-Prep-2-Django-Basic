from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from Fruitipedia.fruits.models import Fruit
from Fruitipedia.profiles.models import Profile


def get_profile():
    try:
        profile = Profile.objects.first()
        return profile
    except Exception:
        return None


# Create your views here.
class HomePageView(TemplateView):
    template_name = "common/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        if profile:
            have_profile = False
        else:
            have_profile = True
        context['have_profile'] = have_profile
        return context


class DashboardView(ListView):
    model = Fruit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        if profile:
            have_profile = False
        else:
            have_profile = True
        context['have_profile'] = have_profile
        return context

    template_name = "common/dashboard.html"
