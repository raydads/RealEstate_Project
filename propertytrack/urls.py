from django.urls import path
from . import views

app_name = "propertytrack"

urlpatterns = [
    path("", views.home, name="home"),
    path("test/", views.test_page, name="test"),

    path("rentals/create/", views.rental_create, name="rental_create"),

    path(
        "rental/<int:rental_id>/inspection/create/",
        views.inspection_create,
        name="inspection_create"
    ),

    path(
        "inspection/<int:inspection_id>/",
        views.inspection_detail,
        name="inspection_detail"
    ),

    path(
        "rentals/",
        views.rental_list,
        name="rental_list"
    ),
]