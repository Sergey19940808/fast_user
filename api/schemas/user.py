from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.String(required=True, attribute="_id", description="Id of user")
    email = fields.String(required=True, description="Email of user")
    phone = fields.String(required=True, description="Phone of user")
    name = fields.String(required=True, description="Name of user")