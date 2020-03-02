"""
This module for declaration of class Mongo Store
"""
from api.models.user import UserModel

from libs.store.base import BaseStore


class MongoStore(BaseStore):
    def __init__(self, collection: UserModel):
        self.collection = collection
