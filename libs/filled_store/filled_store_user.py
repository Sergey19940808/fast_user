"""
This module for declaration of class FilledStoreUser
"""
import uuid

from api.models.user import UserModel
from libs.filled_store.base import BaseFilledStore
from libs.store.mongo import MongoStore


class FilledStoreUser(BaseFilledStore):
    def __init__(self, store: MongoStore, cnt_user: int = 1000):
        self.store = store
        self.cnt_user = cnt_user

    def filled(self) -> None:
        """
        Method for filling store collections user
        """
        users = []
        for item in range(self.cnt_user):
            users.append(dict(
                name=f'Sergey_{str(uuid.uuid4())}',
                email=f'sergey_{str(uuid.uuid4())}@mail.ru',
                phone=f'88000000000'
            ))
        self.store.insert_many(users)


if __name__ == '__main__':
    filled_store_user = FilledStoreUser(
       MongoStore(UserModel)
    )
    filled_store_user.filled()