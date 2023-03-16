from rest_framework import status
from rest_framework.views import APIView

# from schoolmanagement_api.apps.subscription.utils import get_subscription_status
from schoolmanagement_api.apps.users.api.v1.serializers import (
    SchoolUserLoginSerializer,
    SchoolUserSerializer,
)
from schoolmanagement_api.apps.users.api.v1.services import UserLoginData, get_user_role
from schoolmanagement_api.apps.utils import CacheUtils, success_response

# Create your views here.


class SchoolUser(APIView):
    def get_serializer(self):
        return SchoolUserSerializer

    def post(self, request):
        try:
            serializer_class = self.get_serializer()
            serializer = serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            # data = get_subscription_status()
            serializer.save()
            # data.update(serializer.validated_data)
            # print(data)
            return success_response(
                status=status.HTTP_200_OK, data=serializer.validated_data
            )

        except Exception as ex:
            raise ex


class SchoolUserLogin(APIView):
    @staticmethod
    def get_cache_key(data: dict):
        return UserLoginData.generate_cache_key(user_data=data)

    def post(self, request):
        try:
            serializer = SchoolUserLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data["email"]

            # TODO: pass password as well if further authentication required

            user_data = get_user_role(email=email)
            data = UserLoginData.parse_data(user_data, email)
            cache_key = self.get_cache_key(data)
            CacheUtils.set_cache(cache_key, user_data)
            # cached_data = CacheUtils.get_cache(cache_key)
            return success_response(status=status.HTTP_200_OK, data=data)
        except Exception as ex:
            raise ex

    @staticmethod
    def get(request):
        CacheUtils.delete_cache()
        return success_response(status=status.HTTP_200_OK, data="Logout successful")
