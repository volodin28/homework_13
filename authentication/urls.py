from django.urls import path

from . import views

urlpatterns = [
    path("sign_up/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.login_view, name="login"),
    path("account/", views.user_account_view, name="account"),
    path("activate/<str:id>/<str:token>/", views.activate, name="activate"),
]
