from django.urls import path

from . import views

urlpatterns = [
    path("", views.cookies_list, name="cookies_list"),
    path("add/", views.add_cookie, name="add_cookie"),
]
