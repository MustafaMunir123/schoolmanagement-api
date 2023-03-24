from django.urls import path

from schoolmanagement_api.apps.school.api.v1.views import SubjectApiView

urlpatterns = [
    path("v1/subject/", SubjectApiView.as_view()),
]
