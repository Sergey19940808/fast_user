"""
This module for declaration of class FilledStoreUser
"""
import uuid
from dataclasses import dataclass

from store.interface import IStore
from store.mongo import MongoStore

from libs.filled_store.base import BaseFilledStore


@dataclass
class FilledStoreUser(BaseFilledStore):
    cnt_user: int

    def filled(self, store: MongoStore = None) -> None:
        """
        Method for filled store collections user
        """
        users = []
        for item in range(self.cnt_user):
            users.append(dict(
                name=f'Sergey_{str(uuid.uuid4())}',
                email=f'sergey_{str(uuid.uuid4())}@mail.ru',
                phone=f'88000000000'
            ))
        store.insert_many(users)


if __name__ == '__main__':
    filled_store_user = FilledStoreUser(
        1000,
    )
    filled_store_user.filled()