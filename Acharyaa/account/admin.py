from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm   # creation form
    form = CustomUserChangeForm         # change form
    model = CustomUser

    list_display = ("first_name","last_name","username", "email","phone", "is_active")
    list_filter = ("username", "email")

    fieldsets = (
        (None, {"fields": ("first_name","last_name","username", "email", "password","phone")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("first_name","last_name","username", "email","phone","groups","password1", "password2", "is_staff", "is_active")}
        ),
    )

    search_fields = ("username", "email")
    ordering = ("username",)
admin.site.register(CustomUser, CustomUserAdmin)