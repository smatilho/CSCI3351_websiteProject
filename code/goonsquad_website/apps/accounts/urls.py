from django.urls import path
from django.contrib.auth import views as auth_views

# from django.views.generic.base import TemplateView

from . import views

app_name = "accounts"
urlpatterns = [
    path("profile", views.ProfileView.as_view(), name="profile"),
    # This is Django Auth stuff
    path(
        "login",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
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
