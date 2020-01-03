"""
This module for declaration a class App
"""
from dataclasses import dataclass

from sanic import Sanic
from sanic_motor import BaseModel

from api.route.route import Route
from config.api_config import ApiConfig
from config.log_config import LogConfig


@dataclass
class App:
    app: Sanic = None

    def __call__(self):
        """
        Method doing class App as a function
        """
        self.create_app()
        self.app.run(
            host=self.app.config.get('HOST'),
            port=self.app.config.get('PORT'),
            debug=self.app.config.get('DEBUG'),
            access_log=self.app.config.get('ACCESS_LOG'),
        )

    def create_app(self) -> None:
        """
        Method for creating instance of app user
        """
        # Init application for user
        app = Sanic('user', log_config=LogConfig.LOGGING)

        # Load the settings
        app = self.add_config(app)

        # Init mongodb
        app = self.add_db(app)

        # Init route for application for user
        app = self.add_routes(app)

        self.app = app

    @staticmethod
    def add_config(app: Sanic) -> Sanic:
        """
        Method for adding config in the instance of app
        """
        app.config.from_object(ApiConfig)
        return app

    @staticmethod
    def add_db(app: Sanic) -> Sanic:
        """
        Method for adding db in the instance of app
        """
        BaseModel.init_app(app)
        return app

    @staticmethod
    def add_routes(app: Sanic) -> Sanic:
        """
        Method for adding routes in the instance of app
        """
        Route(app)()
        return app

