"""
This module for declaration resources app user
"""
from sanic.views import HTTPMethodView
from sanic.response import json

from logging import getLogger


logger = getLogger('sanic.root')


class UserResource(HTTPMethodView):
    async def get(self, request):
        return json({'name': 'Sergey'})
