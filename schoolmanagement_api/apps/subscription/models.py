from datetime import date

from django.db import models

# Create your models here.

SUBSCRIPTION_STATUS_CHOICES = (
    ("active", "active"),
    ("expired", "expired"),
)


class MonthlySubscription(models.Model):
    status = models.CharField(
        choices=SUBSCRIPTION_STATUS_CHOICES,
        default="active",
        blank=False,
        null=False,
        max_length=15,
    )
    date_paid = models.DateField(default=date.today, null=False, blank=False)

    def __str__(self):
        return f"{str(self.status).upper()}---{self.date_paid}"
