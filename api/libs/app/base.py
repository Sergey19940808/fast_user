"""
This module for declaration a class BaseApp
"""
from dataclasses import dataclass
from sanic_motor import BaseModel
from sanic_openapi import swagger_blueprint

from config.log_config import LogConfig
from sanic import Sanic

from api.routes.user import Route
from config.api_config import ApiConfig


@dataclass
class BaseApp:
    app: None

    @staticmethod
    def init_app(name_app: str) -> Sanic:
        """
        Base method for a initialization of app
        """
        return Sanic(name_app, log_config=LogConfig.LOGGING) if ApiConfig.MODE_PROD else Sanic('user')

    @staticmethod
    def add_config(app: Sanic) -> Sanic:
        """
        Base method for adding config in the instance of app
        """
        app.config.from_object(ApiConfig)
        return app

    @staticmethod
    def add_db(app: Sanic) -> Sanic:
        """
        Base method for adding db in the instance of app
        """
        BaseModel.init_app(app)
        return app

    @staticmethod
    def add_routes(app: Sanic) -> Sanic:
        """
        Base method for adding routes in the instance of app
        """
        Route(app)()
        return app

    @staticmethod
    def add_blueprints(app: Sanic) -> Sanic:
        """
        Base method for adding blueprints in the instance of app
        """
        app.blueprint(swagger_blueprint)
        return app
