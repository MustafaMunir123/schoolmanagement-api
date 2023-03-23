from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from schoolmanagement_api.apps.school.constants import (
    CLASS_NAME_CHOICES,
    CLASS_SECTION_CHOICES,
    EXAMS_TYPE,
    GRADES,
)

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject_title = models.CharField(max_length=70, null=False, blank=False)

    def __str__(self):
        return self.subject_title


class Teacher(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=70)
    last_name = models.CharField(blank=False, null=False, max_length=70)
    contact_number = PhoneNumberField(blank=False, null=False, max_length=13)
    email = models.EmailField(blank=True)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Classroom(models.Model):
    class_name = models.CharField(
        blank=False, null=False, choices=CLASS_NAME_CHOICES, max_length=20
    )
    section = models.CharField(
        blank=False, null=False, choices=CLASS_SECTION_CHOICES, max_length=20
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.class_name}-{self.section}"


class Exam(models.Model):
    type = models.CharField(null=False, blank=False, choices=EXAMS_TYPE, max_length=40)
    class_room = models.ManyToManyField(Classroom, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return f"{self.type}---{self.start_date}"


class Student(models.Model):
    first_name_st = models.CharField(max_length=20, blank=False, null=False)
    last_name_st = models.CharField(max_length=20, blank=False, null=False)
    roll_no = models.IntegerField(unique=True, blank=False, null=False)
    dob = models.DateField(blank=False, null=False)
    last_grade = models.CharField(
        null=False, blank=False, choices=GRADES, max_length=10
    )
    first_name_pr = models.CharField(max_length=20, blank=False, null=False)
    last_name_pr = models.CharField(max_length=20, blank=False, null=False)
    contact_number_pr = PhoneNumberField(blank=False, null=False, max_length=13)
    address = models.CharField(max_length=200, blank=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name_st}-{self.last_name_st}--{self.roll_no}--{self.classroom}"
