# Generated by Django 4.1.2 on 2023-03-23 19:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0007_rename_subjects_subject"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Exams",
            new_name="Exam",
        ),
        migrations.RemoveField(
            model_name="student",
            name="previous_grade_achieved",
        ),
        migrations.AlterField(
            model_name="student",
            name="last_grade",
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
                max_length=10,
            ),
        ),
    ]