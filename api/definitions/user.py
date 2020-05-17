from sanic_openapi import doc


class UserDefinition:
    name: doc.String = doc.String(description="Name of user models")
    email: doc.String = doc.String(description="Email of user models")
    phone: doc.String = doc.String(description="Phone of user models")