"""
This module for declaration of interface FilledStoreUser
"""
from abc import ABCMeta, abstractmethod

from libs.store.base import BaseStore


class IFilledStore(metaclass=ABCMeta):
    @abstractmethod
    def filled(self, store: BaseStore) -> None:
        """
        Abstract method for filled of store
        """
        pass
