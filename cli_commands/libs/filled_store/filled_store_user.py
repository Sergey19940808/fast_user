"""
This module for declaration of class FilledStoreUser
"""
import uuid
from dataclasses import dataclass

from cli_commands.libs.store.mongo import MongoStore

from cli_commands.libs.filled_store.base import BaseFilledStore


@dataclass
class FilledStoreUser(BaseFilledStore):
    cnt_user: int = 1000
    store: MongoStore = MongoStore()

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
    filled_store_user = FilledStoreUser()
    filled_store_user.filled()