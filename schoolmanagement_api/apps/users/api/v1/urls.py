from django.urls import path

from schoolmanagement_api.apps.users.api.v1.views import SchoolUser, SchoolUserLogin

urlpatterns = [
    path("v1/create/", SchoolUser.as_view()),
    path("v1/login/", SchoolUserLogin.as_view()),
    path("v1/logout/", SchoolUserLogin.as_view()),
]
