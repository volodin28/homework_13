from django.shortcuts import render

from .models import Cookie


def cookies_list(request):
    cookies = Cookie.objects.all()
    return render(request, "cookies_list.html", {"cookies": cookies})
