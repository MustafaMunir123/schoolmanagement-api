from rest_framework import status
from rest_framework.views import APIView

from schoolmanagement_api.apps.school.api.v1.serializers import (
    SubjectSerializer,
    TeacherSerializer,
)
from schoolmanagement_api.apps.school.models import Subject, Teacher
from schoolmanagement_api.apps.utils import success_response


class SubjectApiView(APIView):
    @staticmethod
    def get_serializer_class():
        return SubjectSerializer

    def post(self, request):
        try:
            serializer = self.get_serializer_class()
            serializer = serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return success_response(
                status=status.HTTP_200_OK, data=serializer.validated_data
            )
        except Exception as ex:
            raise ex

    def get(self, request):
        queryset = Subject.objects.all()
        serializer = self.get_serializer_class()
        serializer = serializer(queryset, many=True)
        return success_response(status=status.HTTP_200_OK, data=serializer.data)

    @staticmethod
    def delete(request):
        try:
            subject = request.data["subject_title"]
            subject = Subject.objects.get(subject_title=subject)
            subject.delete()
            return success_response(
                status=status.HTTP_200_OK,
                data=f"Subject {subject} successfully deleted",
            )
        except Exception as ex:
            raise ex

    @staticmethod
    def put(request):
        try:
            old_subject = request.data["subject_title"]
            new_subject = request.data["new_subject_title"]
            subject = Subject.objects.get(subject_title=old_subject)
            subject.subject_title = new_subject
            subject.save()
            return success_response(
                status=status.HTTP_200_OK,
                data=f"success updating {old_subject} to {new_subject}",
            )
        except Exception as ex:
            raise ex


#
# class StudentApiView(APIView):
#     @staticmethod
#     def get_serializer_class():
#         return StudentSerializer
#
#     def post(self, request):
#         try:
#             serializer = self.get_serializer_class()
#             serializer = serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return success_response(
#                 status=status.HTTP_200_OK, data=serializer.validated_data
#             )
#         except Exception as ex:
#             raise ex
#
#     def get(self, request):
#         try:
#             queryset = Subject.objects.all()
#             serializer = self.get_serializer_class()
#             serializer = serializer(queryset, many=True)
#             return success_response(status=status.HTTP_200_OK, data=serializer.data)
#         except Exception as ex:
#             raise ex
#
#     @staticmethod
#     def delete(request):
#         try:
#             roll_no = request.data["roll_no"]
#             student = Subject.objects.get(subject_title=roll_no)
#             student.delete()
#             return success_response(
#                 status=status.HTTP_200_OK,
#                 data=f"Subject {student} successfully deleted",
#             )
#         except Exception as ex:
#             raise ex
#
#     @staticmethod
#     def put(request):
#         try:
#             old_subject = request.data["subject_title"]
#             new_subject = request.data["new_subject_title"]
#             subject = Subject.objects.get(subject_title=old_subject)
#             subject.subject_title = new_subject
#             subject.save()
#             return success_response(
#                 status=status.HTTP_200_OK,
#                 data=f"success updating {old_subject} to {new_subject}",
#             )
#         except Exception as ex:
#             raise ex


class TeacherApiView(APIView):
    @staticmethod
    def get_id(data):
        teacher = Teacher.objects.get(email=data["email"])
        data["id"] = teacher.id
        return data

    @staticmethod
    def get_serializer_class():
        return TeacherSerializer

    @staticmethod
    def add_subjects(subjects_list, email):
        subjects = []
        for subject in subjects_list:
            subject = Subject.objects.get(subject_title=subject)
            subjects.append(subject.id)
        teacher = Teacher.objects.get(email=email)
        teacher.subjects.add(*subjects)
        teacher.save()

    @staticmethod
    def update_subjects_or_none(data, pk):
        subjects = data.pop("subjects", None)
        if subjects is not None:
            subject_list = []
            for subject in subjects:
                subject_list.append(subject["id"])
            teacher = Teacher.objects.get(id=pk)
            teacher.subjects.set(subject_list)
            teacher.save()

    def post(self, request):
        # TODO: warn from frontend site if the entered name is according to NIC
        try:
            serializer = self.get_serializer_class()
            serializer = serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = self.get_id(serializer.validated_data)
            self.add_subjects(
                subjects_list=request.data["subjects"],
                email=serializer.validated_data["email"],
            )
            return success_response(status=status.HTTP_200_OK, data=data)
        except Exception as ex:
            raise ex

    def get(self, request, pk=None):
        print(f"{pk}--------------------------")
        serializer = self.get_serializer_class()
        queryset = Teacher.objects.all()
        if pk is not None:
            queryset = Teacher.objects.get(id=pk)
            serializer = serializer(queryset)
            return success_response(status=status.HTTP_200_OK, data=serializer.data)
        serializer = serializer(queryset, many=True)
        return success_response(status=status.HTTP_200_OK, data=serializer.data)

    @staticmethod
    def delete(request):
        try:
            if request.data != {}:
                Teacher.objects.get(email=request.data["email"]).delete()
                msg = {
                    "message": f"Teacher with email: {request.data['email']} deleted"
                }
                return success_response(status=status.HTTP_200_OK, data=msg)
            teacher = Teacher.objects.all()
            teacher.delete()
            return success_response(
                status=status.HTTP_200_OK,
                data=f"Teacher {teacher} successfully deleted",
            )
        except Exception as ex:
            raise ex

    def patch(self, request, pk):
        try:
            teacher = Teacher.objects.get(id=pk)
            serializer = self.get_serializer_class()
            serializer = serializer(teacher, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            self.update_subjects_or_none(request.data, pk)
            return success_response(
                status=status.HTTP_200_OK, data=serializer.validated_data
            )
        except Exception as ex:
            raise ex
