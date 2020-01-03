"""
This module for declaration of class BaseFilledStoreUser
"""
from store.base import BaseStore

from libs.filled_store.interface import IFilledStore


class BaseFilledStore(IFilledStore):
    def filled(self, store: BaseStore) -> None:
        """
        Base method for filled of store
        """
        pass