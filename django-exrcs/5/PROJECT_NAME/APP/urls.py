from django.urls import path
from . import views

app_name = "APP"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet")
]