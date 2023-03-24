from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from schoolmanagement_api.apps.school.models import Subject


class SubjectSerializer(serializers.Serializer):
    subject_title = serializers.CharField(allow_null=False, allow_blank=False)

    def create(self, validated_data):
        subject = Subject.objects.create(
            subject_title=validated_data["subject_title"],
        )
        return subject


class TeacherSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        allow_blank=False, allow_null=False, max_length=70
    )
    last_name = serializers.CharField(
        allow_blank=False, allow_null=False, max_length=70
    )
    contact_number = PhoneNumberField(
        allow_blank=False, allow_null=False, max_length=13
    )
    email = serializers.EmailField(allow_blank=True)
    subjects = SubjectSerializer


class ClassroomSerializer(serializers.Serializer):
    class_name = serializers.CharField(
        allow_null=False, allow_blank=False, max_length=20
    )
    section = serializers.CharField(allow_blank=False, allow_null=False, max_length=20)
    teacher = TeacherSerializer


class StudentSerializer(serializers.Serializer):
    first_name_st = serializers.CharField()
    last_name_st = serializers.CharField()
    roll_no = serializers.IntegerField()
    dob = serializers.DateField()
    last_grade = serializers.CharField()
    first_name_pr = serializers.CharField()
    last_name_pr = serializers.CharField()
    contact_number_pr = PhoneNumberField()
    address = serializers.CharField(max_length=200)
    classroom = ClassroomSerializer
