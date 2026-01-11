from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["author", "title", "feeling"]
        widgets = {
            "author": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}),
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "What's your plan today?"}),
            "feeling": forms.Select(attrs={"class": "form-select"})
        }
