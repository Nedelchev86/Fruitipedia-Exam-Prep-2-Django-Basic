
from django.urls import path

urlpatterns = [
    path("create/", CreateProfileView.as_view(), name="create_fruit"),
    path("details/", DetailsProfileView.as_view(), name="details_fruit"),
    path("edit/", EditFProfileView.as_view(), name="create_fruit"),
    path("dekete/", DeleteProfileView.as_view(), name="create_fruit"),
]
