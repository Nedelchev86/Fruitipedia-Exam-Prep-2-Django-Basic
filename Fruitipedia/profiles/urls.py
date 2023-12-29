
from django.urls import path

from Fruitipedia.profiles.views import CreateProfileView, DetailsProfileView, DeleteProfileView, EditProfileView

urlpatterns = [
    path("create/", CreateProfileView.as_view(), name="create_profile"),
    path("details/", DetailsProfileView.as_view(), name="details_profile"),
    path("edit/", EditProfileView.as_view(), name="edit_profile"),
    path("delete/", DeleteProfileView.as_view(), name="delete_profile"),
]
