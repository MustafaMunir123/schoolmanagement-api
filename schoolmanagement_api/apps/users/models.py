from datetime import datetime

from django.db import models

# Create your models here.
USER_ROLE_CHOICES = (
    ("Teacher", "Teacher"),
    ("Finance", "Finance"),
)


class SchoolUser(models.Model):
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
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
    date_joined = models.DateTimeField(default=datetime.today())

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
