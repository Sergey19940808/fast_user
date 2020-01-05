"""
This module for declaration of interface Store
"""
from abc import ABCMeta, abstractmethod


class IStore(metaclass=ABCMeta):
    @abstractmethod
    def get(self) -> None:
        """
        Abstract method for getting document of collection
        """
        pass

    def filter(self) -> None:
        """
        Abstract method for filtering of collection
        """
        pass

    def insert_one(self) -> None:
        """
        Abstract method for inserting of one document
        """
        pass

    def insert_many(self) -> None:
        """
        Abstract method for inserting of many document
        """
        pass