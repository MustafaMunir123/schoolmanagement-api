from django.urls import include, path

urlpatterns = [path("users/", include("schoolmanagement_api.apps.users.api.v1.urls"))]
