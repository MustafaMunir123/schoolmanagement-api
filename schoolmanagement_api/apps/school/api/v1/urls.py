from django.urls import path

from schoolmanagement_api.apps.school.api.v1.views import SubjectApiView, TeacherApiView

urlpatterns = [
    path("v1/subject/", SubjectApiView.as_view()),
    path("v1/teacher/", TeacherApiView.as_view()),
    path("v1/teacher/get/", TeacherApiView.as_view()),
    path("v1/teacher/get/<uuid:pk>", TeacherApiView.as_view()),
    path("v1/teacher/update/<uuid:pk>", TeacherApiView.as_view()),
]
