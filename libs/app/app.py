"""
This module for declaration a class App
"""
from dataclasses import dataclass
from sanic import Sanic

from libs.app.interface import IApp

from libs.app.base import BaseApp
from config.api_config import ApiConfig
from config.log_config import LogConfig


@dataclass
class App(BaseApp, IApp):
    app: Sanic = None

    def __call__(self):
        """
        Method doing class App as a function
        """
        self.create_app()
        # https://github.com/Relrin/sanic-mongodb-extension
        # Connecting ODM
        self.app.run(
            host=self.app.config.get('HOST'),
            port=self.app.config.get('PORT'),
            debug=self.app.config.get('DEBUG'),
            access_log=self.app.config.get('ACCESS_LOG'),
        )

    def create_app(self) -> None:
        """
        Method for creating instance of app
        """
        # Init application for user
        is_prod = ApiConfig.MODE_PROD
        app = Sanic('user', log_config=LogConfig.LOGGING) if is_prod else Sanic('user')

        # Load the settings
        app = self.add_config(app)

        # Init mongodb
        app = self.add_db(app)

        # Init route for application for user
        app = self.add_routes(app)

        self.app = app

