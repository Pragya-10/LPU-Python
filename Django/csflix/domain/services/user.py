from domain.models import User
from main.models import User as UserStoreModel


class UserService:
    def __init__(self, user_model):
        self._user_model = user_model

    def get_user_by_id(self, user_id):
        store_user = self._user_model.objects.get(pk = user_id)
        interests = [
            interest.tag.name
            for interest in store_user.interests.all()
        ]

        return User(
            id=store_user.id,
            name=store_user.first_name + " " + store_user.last_name,
            email=store_user.email,
            interests=interests,
            last_viewed=None
        )

def get_user_service():
    return UserService(
        user_model=UserStoreModel
    )
