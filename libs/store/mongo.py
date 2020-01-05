"""
This module for declaration of class Mongo Store
"""
from libs.store.base import BaseStore
from libs.store.interface import IStore


class MongoStore(BaseStore, IStore):
    pass
