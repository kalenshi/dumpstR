import uuid

from django.core.validators import EmailValidator
from django.template.defaultfilters import slugify
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """
    Custom user Manager that supports using email instead of username
    """

    def create_user(self, first_name, last_name, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password in the database
        Args:
          first_name (str): first name of the user
          last_name (str): last name of the user
          email (str): unique email of the user
          password (str): password to Encrypt and save in the database
          **extra_fields: key-value pairs to add to the user

        Returns:
            User: created user
        Raises:
          ValueError: if the email is not provided
        """
        if not email:
            raise ValueError('Email is  required field')
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        """
        Creates and saves a SuperUser with the given email and password in the database
        Args:
          first_name (str): first name of the user
          last_name (str): last name of the user
          email (str): unique email of the user:
          password (str): password to Encrypt and save in the database
          **extra_fields: key-value pairs to add to the user

        Returns:
            User: created user
        Raises:
          ValueError: if the email is not provided
        """
        superuser = self.create_user(first_name, last_name, email, password, **extra_fields)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    """
    The custom user model that supports email instead of username
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dob = models.DateField(blank=True, null=True)
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    slug = models.SlugField(default=" ", blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        """
        Returns the String representation of the user
        Returns:
          str: String representation of the user
        """
        return f"{self.first_name} {self.email}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.first_name} {self.last_name}")
        super(User, self).save(*args, **kwargs)


class Contact(models.Model):
    """
    The contact model that
    """
    company = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, validators=[EmailValidator, ])
    contact = models.CharField(max_length=100, help_text="Person to Contact")
    phone = models.CharField(
        max_length=11, help_text="Contact Phone Number", null=True, blank=True
    )
    message = models.TextField(blank=True, null=True, default="No Message Provided")

    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
