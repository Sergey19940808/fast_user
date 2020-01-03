"""
This module for declaration models
"""
from sanic_motor import BaseModel


class User(BaseModel):
    __coll__ = 'users'
    __unique_fields__ = ['name', 'email']