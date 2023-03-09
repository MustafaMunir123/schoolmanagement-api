from django.contrib import admin

from schoolmanagement_api.apps.users.models import SchoolUser

# Register your models here.


class SchoolUserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]


admin.site.register(SchoolUser, SchoolUserAdmin)
