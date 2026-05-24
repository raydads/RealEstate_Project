from django.urls import path
from . import views

app_name = "prospects"

urlpatterns = [
    path("inspection/<int:inspection_id>/create/", views.prospect_create, name="prospect_create"),
    path("search/", views.prospect_search, name="prospect_search"),
]