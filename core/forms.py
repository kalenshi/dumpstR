from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        label='First Name',
        max_length=80,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your first name"
            },
        )
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=80,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your last name"
            },
        )
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email"
            }
        )
    )
    confirm_email = forms.EmailField(
        label="Confirm Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm Email"
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password"
            }
        )
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm Password"
            }
        )
    )
    dob = forms.DateField(
        label="Birthday",
        widget=forms.DateInput(
            attrs={
                "type": "",
                "class": "form-control"
            }
        ),
        required=False
    )

    class Meta:
        model = get_user_model()
        fields = (
            "first_name", "last_name", "email", "confirm_email", "password1", "password2", "dob"
        )


class LoForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
                "class": "form-control",

            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                "class": "form-control",
            }
        )
    )
