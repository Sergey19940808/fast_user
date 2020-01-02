"""
This module for declaration routes for user of resource
"""
from api.resource.resource import UserResource


class Route:
    def add_routes(self, app):
        app.add_route(UserResource.as_view(), '/')