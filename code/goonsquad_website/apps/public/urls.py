from django.urls import path
from . import views

# from django.views.generic.base import TemplateView

app_name = "public"

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    # path("contact", views.contact, name="contact"),
]
