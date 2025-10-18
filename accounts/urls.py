from django.urls import path
from .views import SignUpView, LogoutView, AccountSettingsView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("settings/", AccountSettingsView.as_view(), name="settings"),
]