from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter username'
        })

        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter email address'
        })

        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter password'
        })

        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm password'
        })