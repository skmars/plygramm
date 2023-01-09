from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class UserLoginForm(AuthenticationForm):
    nickname = forms.CharField(
        label="Nickname", widget=forms.TextInput(attrs={"class": "form-controll"})
    )
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-controll"})
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["nickname"].widget.attrs["placeholder"] = "Nickname"
        self.fields["password"].widget.attrs["placeholder"] = "Password"
