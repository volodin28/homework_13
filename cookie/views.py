from django.shortcuts import render


def index(request):
    return render(request, "../factory/templates/factory/../factory/templates/index.html")
