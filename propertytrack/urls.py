from django.urls import path
from . import views

app_name = "propertytrack"

urlpatterns = [
    # Home
    path("", views.home, name="home"),
    path("test/", views.test_page, name="test"),

    # Rentals
    path("rentals/", views.rental_list, name="rental_list"),
    path("rentals/create/", views.rental_create, name="rental_create"),
    path("rentals/archive/", views.rental_archive_list, name="rental_archive_list"),
    path("rentals/<int:pk>/", views.rental_detail, name="rental_detail"),
    path("rentals/<int:pk>/property-details/", views.property_details, name="property_details"),
    path("rentals/<int:pk>/update/", views.rental_update, name="rental_update"),
    path("rentals/<int:pk>/archive/", views.rental_archive, name="rental_archive"),
    path("rentals/<int:pk>/unarchive/", views.rental_unarchive, name="rental_unarchive"),
    path("rentals/<int:pk>/delete/", views.rental_delete, name="rental_delete"),

    # Inspections
    path("rentals/<int:rental_id>/inspections/", views.inspection_list, name="inspection_list"),
    path("rentals/<int:rental_id>/inspection/create/", views.inspection_create, name="inspection_create"),
    path("rentals/<int:rental_id>/in-inspection/", views.in_inspection, name="in_inspection"),
    path("rentals/<int:rental_id>/completed/", views.completed_inspections_property, name="completed_inspections_property"),
    
    path("inspection/<int:inspection_id>/", views.inspection_detail, name="inspection_detail"),
    path("inspection/<int:inspection_id>/edit/", views.inspection_edit, name="inspection_edit"),
    path("inspection/<int:inspection_id>/statistics/", views.inspection_statistics, name="inspection_statistics"),
    
    path("inspections/completed/", views.completed_inspections, name="completed_inspections"),
    path("inspections/upcoming/", views.upcoming_inspections, name="upcoming_inspections"),
]