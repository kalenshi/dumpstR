from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _

from core.forms import UserRegistrationForm


# Create your views here.

def home(request):
    context = {"title": "Home"}
    msg = _("Welcome to DumpstR")
    messages.add_message(request, messages.SUCCESS, msg)
    return render(request, 'home.html', context)


def login_view(request):
    """
    Route for loging in users to the system
    Args:
        request:

    Returns:
        HttpResponse:
    """
    context = {"title": "Login"}
    if request.user.is_authenticated:
        return redirect('core:accounts', pk=request.user.id)
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('email'),
            password=request.POST.get('password')
        )

        if user is not None:
            login(request, user)
            remember_me = request.POST.get('remember_me')
            if remember_me is not None:
                # request.session.set_expiry(1209600)  # set session to expire after 2 weeks
                pass
            next_page = request.GET.get("next")
            return redirect(next_page) if next_page else redirect(f"/accounts/{user.pk}")
        else:
            msg = _("Check your email and password")
            messages.add_message(request, messages.WARNING, msg)
            return redirect("core:login")
    return render(request, 'accounts/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    msg = _("You have been logged out")
    messages.add_message(request, messages.INFO, msg)

    return redirect("core:home")


@login_required
def account(request, pk):
    user = request.user
    context = {"title": "Account", "user": request.user}
    return render(request, "accounts/account.html", context)


@login_required(login_url="/accounts/login/")
def dashboard(request):
    context = {
        "title": request.user.slug, "user": request.user,
        "looper": ['a', 'h', 'j', 'b', 'c', 'd', 'k', 'l']
    }
    return render(request, "dashboard.html", context)


def about(request):
    context = {"title": "About"}
    return render(request, "about.html", context)


def search_results(request):
    query = request.GET.get("search_query")
    if query is not None:
        context = {"users": "users"}
        return render(request, "search_results.html", context)
    else:
        # users = User.objects.all()
        context = {"users": "users"}
        return render(request, "search_results.html", context)


def running(request, *args, **kwargs):
    context = {"title": "running"}
    return render(request, "running.html", context)


def software_development(request, *args, **kwargs):
    context = {"title": "Software Development"}
    return render(request, "software.html", context)


def mathematics(request, *args, **kwargs):
    context = {"title": "Mathematics"}
    return render(request, "mathematics.html", context)


def contact(request, *args, **kwargs):
    context = {"title": "Contact"}
    return render(request, "contact.html", context)


def blog(request, *args, **kwargs):
    context = {"title": "Blog"}
    return render(request, "blog.html", context)
