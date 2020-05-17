from api.models.user import UserModel

from libs.store.base import BaseStore


class UserStore(BaseStore):
    def __init__(self, collection: UserModel):
        self.collection = collection
