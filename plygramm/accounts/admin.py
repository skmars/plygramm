from typing import Literal

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAccountAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Account


class AddAccountForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("email", "role")

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit: Literal[True]):
        account = super().save(commit=False)
        account.set_paasword(self.cleaned_data["password1"])
        if commit:
            account.save()
        return account


class UpdateAccountForm(forms.ModelForm):
    """
    Doesn't allow changing password in the Admin.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ("email", "password", "role", "is_active", "is_staff")

    def clean_password(self):
        return self.initial["password"]


class AccountAdmin(BaseAccountAdmin):
    form = UpdateAccountForm
    add_form = AddAccountForm

    list_display = ("email", "role", "nickname", "is_staff")
    list_filter = ("is_staff",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "role",
                    "nickname",
                    "account_image",
                    "controll_question",
                    "answer_controll_question",
                )
            },
        ),
        ("Permissions", {"fields": ("is_active", "is_staff", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "role",
                    "password1",
                    "password2",
                    "nickname",
                    "account_image",
                    "controll_question",
                    "answer_controll_question",
                ),
            },
        ),
    )
    search_fields = (
        "email",
        "nickname",
    )
    ordering = (
        "email",
        "nickname",
        "role",
        "account_image",
        "controll_question",
        "answer_controll_question",
    )
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)
