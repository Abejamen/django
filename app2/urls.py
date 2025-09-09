from django.urls import path
from . import views

urlpatterns = [
    path("v1/", views.vista1, name="app2-v1"),
    path("v2/", views.vista2, bame="app2-v2"),
]