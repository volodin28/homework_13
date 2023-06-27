from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


# send_mail('Subject here', 'Here is the message.', '3volodin28@gmail.com', ['2volodin28@gmail.com'],
#           fail_silently=False)
