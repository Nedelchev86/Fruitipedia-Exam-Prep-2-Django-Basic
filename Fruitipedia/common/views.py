from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from Fruitipedia.fruits.models import Fruit
from Fruitipedia.profiles.models import Profile


def get_profile():
    try:
       profile = Profile.objects.first()
    except Exception:
        return False
    return True

# Create your views here.
class HomePageView(TemplateView):
    template_name = "common/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["have_profile"] = get_profile()
        return context


class DashboardView(ListView):
    model = Fruit
    template_name = "common/dashboard.html"
