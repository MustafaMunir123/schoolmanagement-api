from django.urls import include, path

urlpatterns = [
    path("users/", include("schoolmanagement_api.apps.users.api.v1.urls")),
    path("school/", include("schoolmanagement_api.apps.school.api.v1.urls")),
]
