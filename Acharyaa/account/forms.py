from django import forms
from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(AdminUserCreationForm):
    role = forms.ChoiceField(
        choices=CustomUser._meta.get_field("role").choices,
        required=True
    )
    phone = forms.CharField(required=False)
    class Meta:
        model = CustomUser
        fields = ("username", "email","role","phone",)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email","role","phone",)