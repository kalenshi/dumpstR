from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from core.forms import UserRegistrationForm


def register(request, *args, **kwargs):
    context = {"title": "Register"}
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            send_mail(
                subject="Activate your account",
                html_message=render_to_string("accounts/activation_email.html", {"token": user.uuid}),
                from_email="from@example.com",
                recipient_list=[email, ],
                fail_silently=False,
            )
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, _("Successfully registered!"))
                return redirect("core:accounts", pk=user.pk)
            else:
                messages.error(request, _("Unable to Authenticate"))
                return redirect("core:register")

        else:
            print(form.errors)
    else:
        context["form"] = UserRegistrationForm()
    return render(request, "accounts/register.html", context)
