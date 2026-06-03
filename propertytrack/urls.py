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
        "rentals/<int:pk>/update/",
        views.rental_update,
        name="rental_update"
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

    path(
        "rentals/<int:pk>/", 
        views.rental_detail, 
        name="rental_detail"),
    
    path(
        "rental/<int:rental_id>/inspections/",
        views.inspection_list,
        name="inspection_list"
    ),

    path(
        "rentals/<int:rental_id>/in-inspection/",
         views.in_inspection,
        name="in_inspection"),
    
    path(
        "inspection/<int:inspection_id>/edit/",
        views.inspection_edit,
        name="inspection_edit"
    ),

    path(
        "inspection/<int:inspection_id>/statistics/",
        views.inspection_statistics,
        name="inspection_statistics"
    ),

    path("inspections/completed/",
     views.completed_inspections,
      name="completed_inspections"),


]