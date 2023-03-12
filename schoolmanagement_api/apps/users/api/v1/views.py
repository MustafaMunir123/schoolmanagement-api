from rest_framework import status
from rest_framework.views import APIView

# from schoolmanagement_api.apps.subscription.utils import get_subscription_status
from schoolmanagement_api.apps.users.api.v1.serializers import SchoolUserSerializer
from schoolmanagement_api.apps.utils import success_response

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
