import uuid

from asyncio import new_event_loop, set_event_loop, ensure_future
from typing import Coroutine

from clients import MongoClient
from filled_store.base import BaseFilledStore
from store.user import UserStore


class FilledStoreUser(BaseFilledStore):
    def __init__(self, store: UserStore, cnt_user: int = 10000):
        self.store = store
        self.cnt_user = cnt_user

    async def filled(self) -> Coroutine:
        """
        Method for filling store collections user
        """
        users = []
        for item in range(self.cnt_user):
            users.append(dict(
                name=f"Sergey_{str(uuid.uuid4())}",
                email=f"sergey_{str(uuid.uuid4())}@mail.ru",
                phone=f"88000000000"
            ))
        return await self.store.insert_many(users)


if __name__ == "__main__":
    loop = new_event_loop()
    set_event_loop(loop)
    filled_store_user = FilledStoreUser(
        UserStore(
            "users",
            MongoClient(loop)()
        ),
    )
    future_filled_store_user = ensure_future(filled_store_user.filled())
    loop.run_until_complete(future_filled_store_user)
