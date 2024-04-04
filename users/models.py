from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Add custom fields or methods here

    # Profile Image field
    # To use ImageField class, you need to install Pillow first
    # python -m pip install Pillow
    profile_image = models.ImageField(
        "Profile Image", upload_to = "users/profile", blank = True
    )

    # Short Description field
    short_description = models.TextField("Introduction", blank = True)

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


