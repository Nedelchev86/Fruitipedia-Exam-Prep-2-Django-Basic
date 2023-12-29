
from django.urls import path

from Fruitipedia.common.views import HomePageView, DashboardView

urlpatterns = [
    path("", HomePageView.as_view(), name="HomePage"),
    path("dashboard/", DashboardView.as_view(), name="dashboard")
]
