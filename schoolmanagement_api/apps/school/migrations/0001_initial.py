# Generated by Django 4.1.2 on 2023-03-24 22:43

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Classroom",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "class_name",
                    models.CharField(
                        choices=[
                            ("Other", "Other"),
                            ("Nursery", "Nursery"),
                            ("KG-1", "KG-1"),
                            ("KG-2", "KG-2"),
                            ("PlayGroup", "PlayGroup"),
                            ("I", "I"),
                            ("II", "II"),
                            ("III", "III"),
                            ("IV", "IV"),
                            ("V", "V"),
                            ("VI", "VI"),
                            ("VII", "VII"),
                            ("VIII", "VIII"),
                            ("IX", "IX"),
                            ("X", "X"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "section",
                    models.CharField(
                        choices=[
                            ("A", "A"),
                            ("B", "B"),
                            ("C", "C"),
                            ("D", "D"),
                            ("E", "E"),
                            ("F", "F"),
                            ("G", "G"),
                            ("H", "H"),
                            ("I", "I"),
                            ("J", "J"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="School",
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
                ("name", models.CharField(max_length=150)),
                ("address", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
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
                ("subject_title", models.CharField(max_length=70, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("first_name", models.CharField(max_length=70)),
                ("last_name", models.CharField(max_length=70)),
                (
                    "contact_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=13, region=None
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("subjects", models.ManyToManyField(to="school.subject")),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("first_name_st", models.CharField(max_length=20)),
                ("last_name_st", models.CharField(max_length=20)),
                ("roll_no", models.IntegerField(unique=True)),
                ("dob", models.DateField()),
                (
                    "last_grade",
                    models.CharField(
                        choices=[
                            ("None", "None"),
                            ("F", "F"),
                            ("D-", "D-"),
                            ("D", "D"),
                            ("D+", "D+"),
                            ("C-", "C-"),
                            ("C", "C"),
                            ("C+", "C+"),
                            ("B-", "B-"),
                            ("B", "B"),
                            ("B+", "B+"),
                            ("A-", "A-"),
                            ("A", "A"),
                            ("A+", "A+"),
                        ],
                        max_length=10,
                    ),
                ),
                ("first_name_pr", models.CharField(max_length=20)),
                ("last_name_pr", models.CharField(max_length=20)),
                (
                    "contact_number_pr",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=13, region=None
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=200)),
                (
                    "classroom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="school.classroom",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Exam",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("MidTerm", "MidTerm"),
                            ("Monthly", "Monthly"),
                            ("Annual", "Annual"),
                            ("Board", "Board"),
                        ],
                        max_length=40,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("class_room", models.ManyToManyField(to="school.classroom")),
            ],
        ),
        migrations.AddField(
            model_name="classroom",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="school.teacher"
            ),
        ),
    ]
