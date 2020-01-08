from dataclasses import dataclass

from sanic_openapi import doc


@dataclass
class User:
    name: doc.String = doc.String(description='Name of user model')
    email: doc.String = doc.String(description='Email of user model')
    phone: doc.String = doc.String(description='Phone of user model')