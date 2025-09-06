from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(AdminUserCreationForm):
    groups = forms.ModelMultipleChoiceField(  
        queryset=Group.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple  # you can use SelectMultiple if you prefer
    )
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    class Meta:
        model = CustomUser
        fields = ("username", "email","phone", "groups")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email","phone",)