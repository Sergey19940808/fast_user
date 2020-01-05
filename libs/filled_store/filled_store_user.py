"""
This module for declaration of class FilledStoreUser
"""
import uuid
from dataclasses import dataclass

from libs.filled_store.interface import IFilledStore

from libs.decorator.di import provider
from libs.store.mongo import MongoStore

from libs.filled_store.base import BaseFilledStore


@dataclass
class FilledStoreUser(BaseFilledStore, IFilledStore):
    cnt_user: int = 1000

    # @provider
    def filled(self, store: MongoStore = None) -> None:
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
        store.insert_many()