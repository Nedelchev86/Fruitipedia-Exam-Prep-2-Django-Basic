from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "common/index.html"


class DashboardView(TemplateView):
    template_name = "common/dashboard.html"