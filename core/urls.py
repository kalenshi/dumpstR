from django.urls import path

from core.views.register_view import register
from core.views.views import (
    home, login_view,
    logout_view, account,
    dashboard, about,
    search_results,
    running,
    software_development,
    mathematics,
    contact,
    blog,
)

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path("about/", about, name='about'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout', logout_view, name='logout'),
    path('accounts/register', register, name='register'),
    path('accounts/<int:pk>/', account, name='accounts'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path("dashboard/", dashboard, name='dashboard'),
    path("dashboard/", dashboard, name='dashboard'),
    path("mathematics/", mathematics, name='mathematics'),
    path("running/", running, name='running'),
    path("software/", software_development, name='software-development'),
    path("search/", search_results, name='-search'),
]
