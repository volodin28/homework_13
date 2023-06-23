from django.shortcuts import render, redirect

from .models import Cookie
from .forms import CookieForm


def cookies_list(request):
    cookies = Cookie.objects.all()
    return render(request, "cookies_list.html", {"cookies": cookies})


def add_cookie(request):
    if request.method == "POST":
        form = CookieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cookies_list")
    else:
        form = CookieForm()
    context = {"form": form}
    return render(request, "add_cookie.html", context)
