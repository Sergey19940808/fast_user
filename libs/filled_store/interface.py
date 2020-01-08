"""
This module for declaration of interface FilledStoreUser
"""
from abc import ABCMeta, abstractmethod


class IFilledStore(metaclass=ABCMeta):
    @abstractmethod
    def filled(self) -> None:
        """
        Abstract method for filled of store
        """
        pass
