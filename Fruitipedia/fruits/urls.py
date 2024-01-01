
from django.urls import path

from Fruitipedia.fruits.views import CreateFruitView, DetailsFruitView, EditFruitView, \
    delete_fruit_form

urlpatterns = [
    path("create/", CreateFruitView.as_view(), name="create_fruit"),
    path("<int:pk>/details/", DetailsFruitView.as_view(), name="details_fruit"),
    path("<int:pk>/edit/", EditFruitView.as_view(), name="edit_fruit"),
    path("<int:pk>/delete/", delete_fruit_form, name="delete_fruit"),
]

