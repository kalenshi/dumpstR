from django.urls import path

from .views.contact_view import ContactEnrollView

app_name = "api"

urlpatterns = [
    path("contact", ContactEnrollView.as_view(), name="contact-enroll"),
]
