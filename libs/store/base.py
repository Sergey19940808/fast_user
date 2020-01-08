"""
This module for declaration of class Base Store
"""
from dataclasses import dataclass
from typing import Any


@dataclass
class BaseStore:
    collection: None

    def find(self) -> None:
        """
        Base method for finding all elements of collection
        """
        return self.collection.find()

    def find_one(self, **kwargs: dict) -> None:
        """
        Base method for finding single element of collection
        """
        return self.collection.find_one(**kwargs)

    def insert_one(self, obj: Any) -> None:
        """
        Base method for inserting of one document
        """
        return self.collection.insert_one(obj)

    def insert_many(self, objs: [Any]) -> None:
        """
        Base method for inserting of many document
        """
        return self.collection.insert_many(objs)
