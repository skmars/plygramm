from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account


class SignUpForm(UserCreationForm):
    nickname = forms.CharField(
        label="Nickname",
        help_text="Nickname must: </br>\
                                             - Not already be in use</br>\
                                             - Have at least 3 letters</br>\
                                             - Have at least one number",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    nickname = forms.CharField(
        label="Nickname",
        help_text="Set your unique Nickname. It can't contain spaces",
        widget=forms.TextInput(attrs={"class": "form-controll"}),
    )
    controll_question = forms.CharField(
        label="Check Question",
        help_text="Set your controll question to secure your indentity",
        widget=forms.TextInput(attrs={"class": "form-controll"}),
    )
    answer_controll_question = forms.CharField(
        label="Answer to Check Question",
        help_text="Set your answer to controll question",
        widget=forms.TextInput(attrs={"class": "form-controll"}),
    )
    # role = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(),
    #                                 widget=forms.CheckboxSelectMultiple, required=True
    # )

    # role = forms.ChoiceField(label="Role",
    #                              widget=forms.Select(attrs={'class':'form-control'}))

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs.pop('autofocus')
        del self.fields["password2"]
        self.fields["nickname"].widget.attrs["placeholder"] = "Nickname"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["email"].widget.attrs["placeholder"] = "email@address.nl"
        self.fields["controll_question"].widget.attrs[
            "placeholder"
        ] = "What's the name of your dog?"
        self.fields["answer_controll_question"].widget.attrs["placeholder"] = "Griffin"

    class Meta:
        model = Account
        fields = (
            "nickname",
            "password1",
            "email",
            "controll_question",
            "answer_controll_question",
        )
        labels = {
            "controll_question": "Controll Question",
            "answer_controll_question": "Anwser to Controll Question",
        }


class ChangeControllQuestionForm(forms.Form):
    class Meta:
        model = Account
        fields = ["controll_question", "answer_controll_question"]
        widgets = {
            "controll_question": forms.TextInput(attrs={"class": "form-control"}),
            "answer_controll_question": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_data(self):
        check_qestion = self.cleaned_data
        return check_qestion


class ControllQuestionValidationForm(forms.Form):
    class Meta:
        model = Account
        fields = [""]
