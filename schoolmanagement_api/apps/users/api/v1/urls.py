from django.urls import path

from schoolmanagement_api.apps.users.api.v1.views import SchoolUser

urlpatterns = [
    path("v1/create/", SchoolUser.as_view()),
]
