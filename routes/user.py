
from typing import Any

from sanic import Sanic

from api.resources.user import UserResource


class Route:
    def __init__(self, app):
        self.app = app

    def __call__(self, *args: tuple, **kwargs: dict) -> Any:
        """
         Method doing class Route as a function
        """
        return self.add_routes(self.app)

    def add_routes(self, app: Sanic) -> Any:
        """
        Method for adding routes
        """
        app.add_route(UserResource.as_view(), "/")