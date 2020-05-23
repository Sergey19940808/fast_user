from typing import Any, Coroutine, List, Dict

from motor.motor_asyncio import AsyncIOMotorClient


class BaseStore:
    def __init__(self, collection: str, client: AsyncIOMotorClient):
        self.collection = collection
        self.db = client.get_database()

    async def find_all(self) -> Coroutine:
        """
        Base method for finding all elements of collection
        """
        return await getattr(self.db, self.collection).find()

    async def find_one(self, **kw) -> Coroutine:
        """
        Base method for finding single element of collection
        """
        return await getattr(self.db, self.collection).find_one(**kw)

    async def insert_one(self, item: Dict) -> Coroutine:
        """
        Base method for inserting of one document
        """
        return await getattr(self.db, self.collection).insert_one(item)

    async def insert_many(self, items: List[Dict]) -> Coroutine:
        """
        Base method for inserting of many document
        """
        return await getattr(self.db, self.collection).insert_many(items)
