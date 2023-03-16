from django.core.exceptions import ObjectDoesNotExist

# from schoolmanagement_api.apps.users.exceptions import UserDoesNotExists
from schoolmanagement_api.apps.users.models import SchoolUser


def get_user_role(email: str) -> dict:
    user_obj = SchoolUser.objects.get(email=email)
    if user_obj:
        return {
            "first_name": user_obj.first_name,
            "last_name": user_obj.last_name,
            "role": user_obj.role,
        }
    # TODO: add custom error response
    raise ObjectDoesNotExist(email)


class UserLoginData:
    @staticmethod
    def parse_data(user_data: dict, email: str) -> dict:
        return {
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"],
            "email": email,
            "role": user_data["role"],
        }

    @staticmethod
    def generate_cache_key(user_data: dict) -> str:
        return f"{user_data['first_name']}-{user_data['last_name']}-{user_data['role']}"
