"""
This module for declaration a class for init instance of app
"""
from sanic import Sanic
from sanic_motor import BaseModel

from api.route.route import Route
from config.api_config import ApiConfig
from config.log_config import LogConfig


class App:
    def __init__(self):
        """

        """
        self.app = None
        self.create_app()

    def __call__(self):
        """

        :return:
        """
        self.app.run(
            host=self.app.config.get('HOST'),
            port=self.app.config.get('PORT'),
            debug=self.app.config.get('DEBUG'),
            access_log=self.app.config.get('ACCESS_LOG'),
        )

    def create_app(self):
        """
        Method for creating instance of app user
        :return:
        """
        # Init application for user
        app = Sanic('user', log_config=LogConfig.LOGGING)

        # Load the settings
        app.config.from_object(ApiConfig)

        # Init mongodb
        BaseModel.init_app(app)

        # Init route for application for user
        route = Route()
        route.add_routes(app)

        self.app = app

