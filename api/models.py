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


def cast_default():
    """
    Returns an empty list if no cast is available
    Returns:
        list: empty list if no cast is available
    """
    return []


class NetflixMovies(models.Model):
    """
    Class representing a Netflix Movies/Series
    """
    show_id = models.CharField(max_length=20)
    show_type = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=80)
    cast = models.JSONField(default=cast_default)
    country = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=False)
    release_year = models.DateField()
    rating = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    listed_in = models.CharField(max_length=255)
    description = models.TextField(default=[])

    def __str__(self):
        """
        String representation of a Netflix Movies/Series
        Returns:
        """
        return f"{self.show_id} : {self.title}"
