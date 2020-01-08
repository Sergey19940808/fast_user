"""
This module for declaration of interface Store
"""
from abc import ABCMeta, abstractmethod
from typing import Any


class IStore(metaclass=ABCMeta):
    @abstractmethod
    def find(self) -> None:
        """
        Abstract method for finding all elements of collection
        """
        pass

    def find_one(self, **kwargs: dict) -> None:
        """
        Abstract method for finding single element of collection
        """
        pass

    def insert_one(self, obj: Any) -> None:
        """
        Abstract method for inserting of one document
        """
        pass

    def insert_many(self, obj: [Any]) -> None:
        """
        Abstract method for inserting of many document
        """
        pass