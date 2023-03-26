from rest_framework import serializers

from schoolmanagement_api.apps.school.models import Subject, Teacher


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "subject_title"]


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            "id",
            "first_name",
            "last_name",
            "contact_number",
            "email",
            "subjects",
        ]
        depth = 1

    def create(self, validated_data):
        teacher = Teacher.objects.create(**validated_data)
        return teacher

    def update(self, instance, validated_data):
        teacher = Teacher.objects.filter(id=instance.id).update(**validated_data)
        return teacher
