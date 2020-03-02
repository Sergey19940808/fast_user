"""
This module for declaration resources
"""
from sanic.request import Request
from sanic.views import HTTPMethodView
from sanic.response import json, HTTPResponse

from sanic_openapi import doc

from api.models.user import UserModel
from api.definitions.user import UserDefinition


class UserResource(HTTPMethodView):
    @doc.tag('users')
    @doc.summary('Fetch all users')
    @doc.description('Resource for fetch all users')
    @doc.produces(doc.List(UserDefinition), content_type='application/json')
    async def get(self, request: Request) -> HTTPResponse:
        """
        Resource for get all users
        """
        cur = await UserModel.find(sort='name')
        list_users = []
        for obj in cur.objects:
            dict_user = {}
            for key in ['name', 'email', 'phone']:
                dict_user.update({key: getattr(obj, key)})
            list_users.append(dict_user)
        return json(list_users)
