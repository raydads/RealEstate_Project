from django.urls import path
from . import views

app_name = "propertytrack"

urlpatterns = [
   path("", views.home, name="home"),
   path("test/", views.test_page, name="test"),
]