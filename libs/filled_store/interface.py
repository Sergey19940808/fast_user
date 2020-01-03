"""
This module for declaration of interface FilledStoreUser
"""
from abc import ABCMeta, abstractmethod

from store.interface import IStore


class IFilledStore(ABCMeta):
    @abstractmethod
    def filled(self, store: IStore) -> None:
        """
        Abstract method for filled of store
        """