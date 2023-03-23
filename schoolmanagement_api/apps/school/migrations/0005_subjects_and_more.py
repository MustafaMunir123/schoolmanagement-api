# Generated by Django 4.1.2 on 2023-03-23 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0004_alter_classroom_class_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subjects",
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
                ("subject_title", models.CharField(max_length=70)),
            ],
        ),
        migrations.RenameField(
            model_name="student",
            old_name="contact_number_gr",
            new_name="contact_number_pr",
        ),
        migrations.RenameField(
            model_name="student",
            old_name="first_name_gr",
            new_name="first_name_pr",
        ),
        migrations.RenameField(
            model_name="student",
            old_name="last_name_gr",
            new_name="last_name_pr",
        ),
        migrations.AddField(
            model_name="student",
            name="previous_grade_achieved",
            field=models.CharField(
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
                default=1,
                max_length=10,
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Exams",
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
                (
                    "class_room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="school.classroom",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="teacher",
            name="subjects",
            field=models.ManyToManyField(to="school.subjects"),
        ),
    ]
