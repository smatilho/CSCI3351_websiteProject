"""goonsquad_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from django.contrib.auth import views as auth_views

# from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("goonsquad_website.apps.public.urls")),
    # path('accounts/profile', views.ProfileView.as_view(), name="profile"),
    path("accounts/", include("goonsquad_website.apps.accounts.urls")),
    path("contact/", include("goonsquad_website.apps.contact.urls"))
    # This is Django Auth stuff
]


# Differnt Django Views
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done [name='password_change_done']
# accounts/password_reset [name='password_reset']
# accounts/password_reset/done [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done [name='password_reset_complete']
