from django.contrib import admin

from schoolmanagement_api.apps.school.models import (
    Classroom,
    Exam,
    Student,
    Subject,
    Teacher,
)

# Register your models here.


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ["class_name", "section"]


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "contact_number"]


class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name_st", "roll_no", "contact_number_pr", "classroom"]


class ExamsAdmin(admin.ModelAdmin):
    list_display = ["type", "start_date"]


class SubjectsAdmin(admin.ModelAdmin):
    list_display = ["id", "subject_title"]


admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Exam, ExamsAdmin)
admin.site.register(Subject, SubjectsAdmin)
