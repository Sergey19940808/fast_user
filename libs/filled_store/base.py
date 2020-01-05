"""
This module for declaration of class BaseFilledStoreUser
"""
from libs.store.base import BaseStore


class BaseFilledStore:
    def filled(self, store: BaseStore) -> None:
        """
        Base method for filled of store
        """
        pass