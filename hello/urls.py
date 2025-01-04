from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("maz", views.maz, name="maz"),
    path("david", views.david, name="david")
]