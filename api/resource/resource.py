"""
This module for declaration resources
"""
from sanic.request import Request
from sanic.views import HTTPMethodView
from sanic.response import json, HTTPResponse

from logging import getLogger


logger = getLogger('sanic.root')


class UserResource(HTTPMethodView):
    def get(self, request: Request) -> HTTPResponse:
        """
        Resource for get all users
        :return:
        """
        r = request
        return json({'name': 'Sergey'})
