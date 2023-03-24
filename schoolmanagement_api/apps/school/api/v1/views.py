from rest_framework import status
from rest_framework.views import APIView

from schoolmanagement_api.apps.school.api.v1.serializers import SubjectSerializer
from schoolmanagement_api.apps.school.models import Subject
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


class StudentApiView(APIView):
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
