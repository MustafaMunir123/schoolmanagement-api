from datetime import date

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
USER_ROLE_CHOICES = (
    ("Admin", "Admin"),
    ("Owner", "Owner"),
)


class SchoolUser(models.Model):
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    role = models.CharField(
        max_length=70, choices=USER_ROLE_CHOICES, null=False, blank=False
    )
    is_active = models.BooleanField(
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateField(default=date.today)
    phonenumber = PhoneNumberField(max_length=13, blank=False, null=False, unique=True)
    username = models.CharField(unique=True, max_length=25, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
