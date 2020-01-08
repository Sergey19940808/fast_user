"""
This module for declaration resources
"""
from sanic.request import Request
from sanic.views import HTTPMethodView
from sanic.response import json, HTTPResponse

from sanic_openapi import doc

from logging import getLogger

from api.model.user import User
from api.schema.user import User

logger = getLogger('sanic.root')


class UserResource(HTTPMethodView):
    @doc.tag('users')
    @doc.summary('Fetch all users')
    @doc.description('Resource for fetch all users')
    @doc.produces(doc.List(User), content_type='application/json')
    async def get(self, request: Request) -> HTTPResponse:
        """
        Resource for get all users
        :return:
        """
        data = await User.find(sort='name asc')
        return json(data)
