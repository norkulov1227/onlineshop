from typing import Any
from django import forms
from apps.accounts.models import User
from apps.base.utils.helpers import phone_regex


class UserForm(forms.ModelForm):

    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget= forms.PasswordInput(attrs={"autocomplete" : "new-password"})
    )

    password2 = forms.CharField(
        label=("Password confirmation"),
        strip=False,
        widget= forms.PasswordInput(attrs={"autocomplete" : "new-password"})
    )
    phone = forms.CharField(validators=[phone_regex])
    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get("password1")
        pass2 = cleaned_data.get("password2")
        if pass1 != pass2:
            raise forms.ValidationError("Parollar bir biriga mos emas. Iltimos qayta urinib ko'ring!")
        return cleaned_data
    class Meta:
        model = User
        fields = ['phone']
