# Generated by Django 4.1.2 on 2023-03-12 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MonthlySubscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "active"), ("expired", "expired")],
                        default="active",
                        max_length=15,
                    ),
                ),
                ("data_paid", models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
