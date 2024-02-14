from django.db import models


# Create your models here.

class ContactEnroll(models.Model):
    """
    Class for contacting frontend communications
    """
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=255, unique=True)
    contact_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True, default="No message")
    contacted = models.BooleanField(default=False)

    def __str__(self):
        """
        String representation of ContactEnroll object
        Returns:
            str: a Human readable representation of ContactEnroll object
        """
        return f"{self.first_name} : {self.email}"
