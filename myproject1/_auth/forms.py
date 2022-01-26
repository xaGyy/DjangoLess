from django import forms
from django.contrib.auth.models import User

class createUserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ("username", "password", "email")