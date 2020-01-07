"""
This module for declaration models
"""
from umongo import Document
from umongo.fields import StringField

from libs.db.client import instance, db


@instance.register
class User(Document):
    name = StringField(required=True, allow_none=False)
    email = StringField(required=False, allow_none=True)
    phone = StringField(required=False, allow_none=True)
