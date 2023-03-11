from datetime import datetime

import phonenumbers
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from schoolmanagement_api.apps.users.models import SchoolUser


class SchoolUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        max_length=150, allow_blank=False, allow_null=False
    )
    last_name = serializers.CharField(
        max_length=150, allow_blank=False, allow_null=False
    )
    email = serializers.EmailField(allow_null=False, allow_blank=False)
    role = serializers.CharField(max_length=70, allow_blank=False, allow_null=False)
    is_active = serializers.BooleanField(default=True)
    date_joined = serializers.DateTimeField(default=datetime.today())
    phonenumber = serializers.CharField(max_length=13)
    username = serializers.CharField(allow_blank=False, allow_null=False)
    password = serializers.CharField(max_length=20, min_length=8)

    @staticmethod
    def validate_mobile_number(value):
        phonenumber = phonenumbers.parse(str(value))
        if not phonenumbers.is_possible_number(phonenumber):
            raise Exception
        return phonenumber

    def valiadte_date_joined(self):
        pass

    def create(self, validated_data):
        user = SchoolUser.objects.create(
            username=validated_data["username"],
            password=make_password(validated_data["password"]),
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phonenumber=validated_data["phonenumber"],
            is_active=validated_data["is_active"],
            date_joined=validated_data["date_joined"],
            role=validated_data["role"],
        )
        return user
