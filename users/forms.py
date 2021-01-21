from django import forms
from . import views


class LoginForm(forms.Form):

    user_id = forms.CharField()
    password = forms.CharField()


class SuccessForm(forms.Form):

    pass