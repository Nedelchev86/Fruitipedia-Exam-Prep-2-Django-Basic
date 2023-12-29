
from django.urls import path

from Fruitipedia.fruits.views import CreateFruitView, DetailsFruitView, EditFruitView, DeleteFruitView

urlpatterns = [
    path("create/", CreateFruitView.as_view(), name="create_fruit"),
    path("<int:pk>/details/", DetailsFruitView.as_view(), name="details_fruit"),
    path("<int:pk>/edit/", EditFruitView.as_view(), name="create_fruit"),
    path("<int:pk>/dekete/", DeleteFruitView.as_view(), name="create_fruit"),
]

