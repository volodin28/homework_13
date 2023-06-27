from django import forms
from .models import Cookie


class CookieForm(forms.ModelForm):
    class Meta:
        model = Cookie
        fields = ("name", "full_name", "description", "image")
        labels = {
            "name": "Назва",
            "full_name": "Повна назва",
            "description": "Опис",
            "image": "Зображення",
        }
