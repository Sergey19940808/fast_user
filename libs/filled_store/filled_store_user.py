"""
This module for declaration of class FilledStoreUser
"""
import uuid
from dataclasses import dataclass


@dataclass
class FilledStoreUser:
    cnt_user: int = 1000

    def filled(self):
        """
        Filled store collections user
        :return:
        """
        users = []
        for item in range(self.cnt_user):
            users.append(dict(
                name=f'Sergey_{str(uuid.uuid4())}',
                email=f'sergey_{str(uuid.uuid4())}@mail.ru',
                phone=f'88000000000'
            ))
        User.insert_many(users)


if __name__ == '__main__':
    filled_store_user = FilledStoreUser(1000)
    filled_store_user.filled()