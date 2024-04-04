from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from users.models import User

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {"fields" : ("username", "password")}),
        ("Personal Info", {"fields" : ("first_name", "last_name", "email")}),
        ("Additional Field", {"fields" : ("profile_image", "short_description")}),
        (
            "Authority",
            {
                "fields" : (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        ("Schedule", {"fields" : ("last_login", "date_joined")}),
    ]

