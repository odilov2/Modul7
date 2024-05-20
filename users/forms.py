from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password")

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=56)
    password = forms.CharField(max_length=50)

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
