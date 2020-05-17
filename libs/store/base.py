from dataclasses import dataclass
from typing import Any, Coroutine, Dict

from sanic_motor import BaseModel


@dataclass
class BaseStore:
    collection: Any

    def find_all(self) -> Coroutine:
        """
        Base method for finding all elements of collection
        """
        return self.collection.find()

    def find_one(self, **kwargs) -> Coroutine:
        """
        Base method for finding single element of collection
        """
        return self.collection.find_one(**kwargs)

    def insert_one(self, obj: Any) -> Coroutine:
        """
        Base method for inserting of one document
        """
        return self.collection.insert_one(obj)

    def insert_many(self, objs: [Any]) -> Coroutine:
        """
        Base method for inserting of many document
        """
        return self.collection.insert_many(objs)
