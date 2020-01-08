"""
This module for declaration of class Mongo Store
"""
from dataclasses import dataclass

from api.model.user import User

from libs.store.base import BaseStore
from libs.store.interface import IStore


@dataclass
class MongoStore(BaseStore, IStore):
    collection: User = User()
