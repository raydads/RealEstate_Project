from django.urls import path
from . import views

app_name = "prospects"

urlpatterns = [
    path("inspection/<int:inspection_id>/check/", views.prospect_phone_check, name="prospect_phone_check"),
    path("inspection/<int:inspection_id>/create/<str:phone>/", views.prospect_create, name="prospect_create"),
    path("inspection/<int:inspection_id>/found/<int:prospect_id>/", views.prospect_found, name="prospect_found"),
    path("search/", views.prospect_search, name="prospect_search"),
    path("<int:prospect_id>/", views.prospect_detail, name="prospect_detail"),
    path("<int:prospect_id>/update/", views.prospect_update, name="prospect_update"),
]